from rapidfuzz import fuzz

from backend.participant_models import Evidence


class TranscriptEngine:
    """
    Extracts evidence from participant transcripts.
    """

    def __init__(self, candidate_name: str):
        self.candidate_name = candidate_name.lower()

    def analyze_event(self, participant, transcript: str):

        participant.transcript.append(transcript)

        transcript_lower = transcript.lower()

        similarity = fuzz.partial_ratio(
            self.candidate_name,
            transcript_lower
        )

        if similarity > 70:

            participant.evidence.append(
                Evidence(
                    source="Transcript",
                    score=40,
                    reason=f"Candidate name detected in transcript ({similarity:.1f}%)"
                )
            )

        elif "my name is" in transcript_lower:

            participant.evidence.append(
                Evidence(
                    source="Transcript",
                    score=30,
                    reason="Participant introduced themselves"
                )
            )