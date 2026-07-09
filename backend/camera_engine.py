from backend.participant_models import Evidence

class CameraEngine:

    def process(self, participant):

        if participant.camera_on:

            participant.evidence.append(
                Evidence(
                    source="Camera",
                    reason="Camera remained ON",
                    score=15
                )
            )

            participant.confidence += 15

        else:

            participant.evidence.append(
                Evidence(
                    source="Camera",
                    reason="Camera was OFF",
                    score=0
                )
            )