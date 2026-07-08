class ConfidenceEngine:

    @staticmethod
    def calculate(participant):

        participant.confidence = sum(
            evidence.score
            for evidence in participant.evidence
        )