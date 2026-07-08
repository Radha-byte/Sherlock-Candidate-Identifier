import json
from rapidfuzz import fuzz

from backend.participant_models import Evidence


class MetadataEngine:
    """
    Generates evidence based on participant metadata.
    """

    def __init__(self, metadata_file: str):
        with open(metadata_file, "r") as file:
            self.metadata = json.load(file)

    def analyze(self, participants):

        candidate_name = self.metadata["candidate_name"]

        for participant in participants:

            similarity = fuzz.ratio(
                candidate_name.lower(),
                participant.display_name.lower()
            )

            score = similarity / 5

            participant.evidence.append(
                Evidence(
                    source="Metadata",
                    score=score,
                    reason=f"Display name similarity: {similarity:.1f}%"
                )
            )