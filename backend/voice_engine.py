from backend.participant_models import Evidence


class VoiceEngine:

    def process(self, participant):

        # Remove previous Voice Recognition evidence
        participant.evidence = [
            e for e in participant.evidence
            if e.source != "Voice Recognition"
        ]

        # Simulated voice embedding similarity
        if participant.display_name == "MacBook Pro":

            score = 18
            reason = "Voice embedding matched registered candidate (89%)"

        else:

            score = 3
            reason = "Voice similarity very low"

        participant.evidence.append(
            Evidence(
                source="Voice Recognition",
                score=score,
                reason=reason
            )
        )