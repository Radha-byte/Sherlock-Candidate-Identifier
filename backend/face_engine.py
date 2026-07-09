from backend.participant_models import Evidence


class FaceEngine:

    def process(self, participant):

        # Simulated face matching

        if participant.display_name == "MacBook Pro":

            score = 25

            participant.evidence.append(
                Evidence(
                    source="Face Recognition",
                    score=score,
                    reason="Face embedding matched registered candidate (92%)"
                )
            )

        else:

            participant.evidence.append(
                Evidence(
                    source="Face Recognition",
                    score=2,
                    reason="Face similarity very low"
                )
            )