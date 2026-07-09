class ConfidenceEngine:

    @staticmethod
    def calculate(participant):

        total = sum(
            evidence.score
            for evidence in participant.evidence
        )

        # Cap confidence at 100
        participant.confidence = min(total, 100)

        if participant.confidence >= 80:
            participant.status = "Verified"

        elif participant.confidence >= 60:
            participant.status = "Likely"

        elif participant.confidence >= 40:
            participant.status = "Uncertain"

        else:
            participant.status = "Insufficient Evidence"

        participant.confidence_history.append(
            participant.confidence
        )