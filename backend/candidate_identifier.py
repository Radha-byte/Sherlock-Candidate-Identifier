import json

from backend.metadata_engine import MetadataEngine
from backend.transcript_engine import TranscriptEngine
from backend.confidence_engine import ConfidenceEngine


class CandidateIdentifier:

    def __init__(self, simulator):

        self.simulator = simulator

        self.participants = simulator.get_participants()

        self.metadata_engine = MetadataEngine("data/metadata.json")

        with open("data/metadata.json", "r") as file:
            metadata = json.load(file)

        self.transcript_engine = TranscriptEngine(
            metadata["candidate_name"]
        )

    def process_events(self):

        # Initial metadata analysis
        self.metadata_engine.analyze(self.participants)

        # Process each event
        for event in self.simulator.get_events():

            participant = self.simulator.manager.get_participant(
                event.participant_id
            )

            if event.event_type == "camera_on":
                participant.camera_on = True

            elif event.event_type == "transcript":
                self.transcript_engine.analyze_event(
                    participant,
                    event.text
                )

            ConfidenceEngine.calculate(participant)

    def get_best_candidate(self):

        return max(
            self.participants,
            key=lambda p: p.confidence
        )