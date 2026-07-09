# 🕵️ Sherlock AI Candidate Identifier

> **Real-Time Multi-Evidence AI System for Identifying Interview Candidates During Live Meetings**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)
![AI](https://img.shields.io/badge/Artificial%20Intelligence-Multi--Evidence-success)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

---

# 📌 Project Overview

Sherlock AI Candidate Identifier is an explainable AI system designed to identify the real interview candidate in online meetings using multiple evidence sources instead of relying on a single signal.

The system continuously analyzes meeting participants and combines metadata, transcript analysis, speaking behavior, camera activity, simulated face recognition, and simulated voice recognition into a unified confidence score.

The candidate with the highest confidence is identified in real time while providing transparent AI reasoning for every decision.

---

# ✨ Features

- ✅ Metadata Analysis
- ✅ Transcript Intelligence
- ✅ Camera Activity Detection
- ✅ Speaking Pattern Analysis
- ✅ Simulated Face Recognition
- ✅ Simulated Voice Recognition
- ✅ Confidence Fusion Engine
- ✅ Candidate Ranking
- ✅ Explainable AI Reasoning
- ✅ Live Streamlit Dashboard
- ✅ Investigation PDF Report

---

# 🧠 AI Pipeline

```
Meeting Data
      │
      ▼
Meeting Simulator
      │
      ▼
Participant Manager
      │
      ▼
Metadata Engine
Transcript Engine
Camera Engine
Speaking Engine
Face Engine
Voice Engine
      │
      ▼
Confidence Engine
      │
      ▼
Confidence Fusion
      │
      ▼
Candidate Ranking
      │
      ▼
Dashboard + PDF Report
```

---

# 📊 Dashboard

> Replace the images below with screenshots from your project.

## Dashboard Overview

![Dashboard](screenshots/dashboard.png)

## Evidence Contribution

![Evidence](screenshots/evidence.png)

## Confidence Evolution

![Confidence](screenshots/confidence.png)

---

# 📂 Project Structure

```text
Sherlock-Candidate-Identifier/

backend/
frontend/
data/
tests/
docs/

app.py
README.md
requirements.txt
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Radha-byte/Sherlock-Candidate-Identifier.git
```

Move into project

```bash
cd Sherlock-Candidate-Identifier
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

---

# 📈 AI Evidence Sources

| Evidence | Purpose |
|-----------|---------|
| Metadata | Compare registered candidate information |
| Transcript | Detect self introduction |
| Camera | Monitor participant camera activity |
| Speaking | Measure speaking duration |
| Face Recognition | Simulated face matching |
| Voice Recognition | Simulated voice similarity |

---

# 📄 Investigation Report

The application automatically generates a downloadable PDF investigation report containing

- Candidate Prediction
- Confidence Score
- Evidence Summary
- Meeting Timeline

---

# 🚀 Future Improvements

- Real Face Recognition (InsightFace)
- Speaker Verification
- Deepfake Detection
- Voice Clone Detection
- Multi-camera Tracking
- Real Zoom/Meet Integration
- LLM-based Interview Understanding

---

# 🏗 Architecture

See

```
docs/architecture.md
```

---

# 👨‍💻 Developer

**Radha Rani**

B.Tech CSE Student

VIT Bhopal University

---

# ⭐ If you like this project

Please consider giving it a star ⭐