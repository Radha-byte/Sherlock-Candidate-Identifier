import json

from backend.meeting import MeetingSimulator
from backend.metadata_engine import MetadataEngine
from backend.transcript_engine import TranscriptEngine
from backend.confidence_engine import ConfidenceEngine

simulator = MeetingSimulator("data/meeting_data.json")
simulator.load_events()

participants = simulator.get_participants()

metadata = MetadataEngine("data/metadata.json")
metadata.analyze(participants)

with open("data/metadata.json") as file:
    candidate = json.load(file)["candidate_name"]

transcript_engine = TranscriptEngine(candidate)

for event in simulator.get_events():

    if event.event_type == "transcript":

        participant = simulator.manager.get_participant(
            event.participant_id
        )

        transcript_engine.analyze_event(
            participant,
            event.text
        )

for participant in participants:

    ConfidenceEngine.calculate(participant)

    print("=" * 50)
    print(participant.display_name)
    print("Confidence:", participant.confidence)

    print()

    for evidence in participant.evidence:

        print(
            f"{evidence.source}: {evidence.reason} (+{evidence.score})"
        )