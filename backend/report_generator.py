from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


class ReportGenerator:

    @staticmethod
    def generate(best, simulator):

        styles = getSampleStyleSheet()

        document = SimpleDocTemplate(
            "Sherlock_Report.pdf"
        )

        elements = []

        elements.append(
            Paragraph(
                "<b>Sherlock AI Investigation Report</b>",
                styles["Title"]
            )
        )

        elements.append(Spacer(1, 20))

        elements.append(
            Paragraph(
                f"<b>Predicted Candidate:</b> {best.display_name}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"<b>Confidence:</b> {best.confidence:.2f}%",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"<b>Status:</b> {best.status}",
                styles["Normal"]
            )
        )

        elements.append(Spacer(1, 20))

        elements.append(
            Paragraph(
                "<b>Evidence</b>",
                styles["Heading2"]
            )
        )

        for evidence in best.evidence:

            elements.append(
                Paragraph(
                    f"• <b>{evidence.source}</b>: {evidence.reason}",
                    styles["Normal"]
                )
            )

        elements.append(Spacer(1,20))

        elements.append(
            Paragraph(
                "<b>Meeting Timeline</b>",
                styles["Heading2"]
            )
        )

        for event in simulator.get_events():

            if event.event_type == "participant_join":
                text = f"{event.display_name} joined meeting"

            elif event.event_type == "camera_on":
                text = "Camera turned ON"

            elif event.event_type == "transcript":
                text = event.text

            else:
                text = event.event_type

            elements.append(
                Paragraph(
                    f"{event.timestamp}s - {text}",
                    styles["Normal"]
                )
            )

        elements.append(Spacer(1,20))

        elements.append(
            Paragraph(
                "<b>Final Verdict:</b> VERIFIED CANDIDATE",
                styles["Heading2"]
            )
        )

        document.build(elements)