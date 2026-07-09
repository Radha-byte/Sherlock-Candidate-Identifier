import matplotlib.pyplot as plt
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from backend.meeting import MeetingSimulator
from backend.candidate_identifier import CandidateIdentifier
from backend.report_generator import ReportGenerator

# -------------------------------
# PAGE CONFIG
# -------------------------------

st.set_page_config(
    page_title="Sherlock AI",
    page_icon="🕵️",
    layout="wide"
)

# -------------------------------
# LOAD DATA
# -------------------------------

simulator = MeetingSimulator("data/meeting_data.json")
simulator.load_events()

identifier = CandidateIdentifier(simulator)
identifier.process_events()

participants = simulator.get_participants()
best = identifier.get_best_candidate()
ranked = identifier.get_ranked_candidates()

if best is None:
    st.error("⚠️ Candidate cannot be identified confidently yet.")
    st.stop()

# -------------------------------
# HEADER
# -------------------------------

st.title("🕵️ Sherlock AI Candidate Identifier")
st.caption("Real-Time Multi-Evidence Candidate Detection")

st.divider()

# -------------------------------
# KPI CARDS
# -------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🎯 Prediction", best.display_name)

with c2:
    st.metric("📈 Confidence", f"{best.confidence:.2f}%")

with c3:
    st.metric("👥 Participants", len(participants))

with c4:
    st.metric("🟢 Status", "LIVE")

st.divider()

# -------------------------------
# MAIN LAYOUT
# -------------------------------

left, right = st.columns([2, 1])

# ==========================================
# LEFT COLUMN
# ==========================================

with left:

    st.subheader("👥 Participants")

    for participant in participants:

        winner = (
            participant.participant_id == best.participant_id
        )

        with st.container(border=True):

            if winner:
                st.success("🏆 VERIFIED CANDIDATE")

            st.markdown(f"### {participant.display_name}")

            st.progress(
                min(participant.confidence / 100, 1.0)
            )

            st.write(
                f"Confidence : {participant.confidence:.2f}%"
            )

            if participant.status == "Verified":
                st.success("🟢 VERIFIED")

            elif participant.status == "Likely":
                st.info("🔵 LIKELY")

            elif participant.status == "Uncertain":
                st.warning("🟡 UNCERTAIN")

            else:
                st.error("🔴 INSUFFICIENT EVIDENCE")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "📷 Camera",
                    "ON" if participant.camera_on else "OFF"
                )

            with c2:
                st.metric(
                    "🎤 Speaking",
                    f"{participant.speaking_duration:.0f}s"
                )

            with c3:
                st.metric(
                    "🧠 Evidence",
                    len(participant.evidence)
                )

            if winner:
                st.caption(
                    "Highest confidence based on multi-evidence AI reasoning."
                )

# ==========================================
# RIGHT COLUMN
# ==========================================

with right:

    st.subheader("🧠 AI Reasoning")

    for evidence in best.evidence:

        st.success(
            f"{evidence.source}\n\n{evidence.reason}"
        )

st.divider()

# -------------------------------
# BOTTOM SECTION
# -------------------------------

left_bottom, right_bottom = st.columns(2)

# ==========================================
# LEFT BOTTOM
# ==========================================

with left_bottom:

    st.subheader("📈 Confidence Evolution")

    st.line_chart(best.confidence_history)

    st.divider()

    st.subheader("📊 Evidence Contribution")

    labels = [e.source for e in best.evidence]
    scores = [e.score for e in best.evidence]

    fig, ax = plt.subplots(figsize=(2.5, 2.5))

    ax.pie(
        scores,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig, width="content")

    plt.close(fig)

# ==========================================
# RIGHT BOTTOM
# ==========================================

with right_bottom:

    st.subheader("📋 Meeting Timeline")

    for event in simulator.get_events():

        if event.event_type == "participant_join":
            text = f"{event.display_name} joined meeting"

        elif event.event_type == "camera_on":
            text = "Camera turned ON"

        elif event.event_type == "transcript":
            text = event.text

        else:
            text = event.event_type

        st.write(f"**{event.timestamp}s** — {text}")

st.divider()

st.success(
    f"Current Candidate Prediction → {best.display_name}"
)

# ===============================
# Candidate Ranking
# ===============================

st.divider()

st.subheader("🏆 Candidate Ranking")

for i, participant in enumerate(ranked, start=1):

    if i == 1:
        medal = "🥇"

    elif i == 2:
        medal = "🥈"

    elif i == 3:
        medal = "🥉"

    else:
        medal = "⭐"

    c1, c2, c3, c4 = st.columns([1, 3, 2, 2])

    with c1:
        st.write(medal)

    with c2:
        st.write(participant.display_name)

    with c3:
        st.write(f"{participant.confidence:.2f}%")

    with c4:
        st.write(participant.status)

# -------------------------------
# PDF REPORT
# -------------------------------

ReportGenerator.generate(best, simulator)

with open("Sherlock_Report.pdf", "rb") as pdf:

    st.download_button(
        label="📄 Download Investigation Report",
        data=pdf.read(),
        file_name="Sherlock_Report.pdf",
        mime="application/pdf",
    )