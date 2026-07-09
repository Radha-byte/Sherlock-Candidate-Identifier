import json

from backend.metadata_engine import MetadataEngine
from backend.transcript_engine import TranscriptEngine
from backend.confidence_engine import ConfidenceEngine
from backend.camera_engine import CameraEngine
from backend.speaking_engine import SpeakingEngine
from backend.face_engine import FaceEngine
from backend.voice_engine import VoiceEngine

class CandidateIdentifier:

    def __init__(self, simulator):

        self.camera_engine = CameraEngine()

        self.speaking_engine = SpeakingEngine()

        self.face_engine = FaceEngine()

        self.voice_engine = VoiceEngine()

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
                self.camera_engine.process(participant)
                self.face_engine.process(participant)

            elif event.event_type == "transcript":

                participant.speaking_duration += event.duration
                
                self.transcript_engine.analyze_event(
                    participant,
                    event.text
                )

                self.voice_engine.process(participant)

                self.speaking_engine.process(participant)

            for p in self.participants:
                ConfidenceEngine.calculate(p)

    def get_best_candidate(self):

        return max(
            self.participants,
            key=lambda p: p.confidence
        )
    
    def get_ranked_candidates(self):

        return sorted(
            self.participants,
            key=lambda p: p.confidence,
            reverse=True
        )