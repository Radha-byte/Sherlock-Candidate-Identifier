from backend.meeting import MeetingSimulator
from backend.metadata_engine import MetadataEngine
from backend.confidence_engine import ConfidenceEngine

simulator = MeetingSimulator("data/meeting_data.json")
simulator.load_events()

participants = simulator.get_participants()

engine = MetadataEngine("data/metadata.json")
engine.analyze(participants)

for participant in participants:

    ConfidenceEngine.calculate(participant)

    print("-" * 50)
    print(participant.display_name)
    print(f"Confidence: {participant.confidence:.2f}")

    for evidence in participant.evidence:
        print(evidence.reason)