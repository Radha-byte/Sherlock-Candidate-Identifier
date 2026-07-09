class FusionEngine:

    @staticmethod
    def get_breakdown(participant):

        breakdown = []

        total = participant.confidence

        if total == 0:
            return []

        for evidence in participant.evidence:

            percentage = round(
                (evidence.score / total) * 100,
                1
            )

            breakdown.append({

                "source": evidence.source,

                "score": evidence.score,

                "percentage": percentage

            })

        return breakdown