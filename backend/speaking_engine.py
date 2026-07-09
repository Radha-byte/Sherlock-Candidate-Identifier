from backend.participant_models import Evidence


class SpeakingEngine:

    def process(self, participant):

        # Remove any previous Speaking evidence
        participant.evidence = [
            e for e in participant.evidence
            if e.source != "Speaking"
        ]

        duration = participant.speaking_duration

        if duration >= 30:
            score = 20
            reason = f"Spoke for {duration:.0f} seconds"

        elif duration >= 15:
            score = 10
            reason = f"Spoke for {duration:.0f} seconds"

        else:
            score = 0
            reason = "Very little speaking activity"

        participant.evidence.append(
            Evidence(
                source="Speaking",
                score=score,
                reason=reason
            )
        )