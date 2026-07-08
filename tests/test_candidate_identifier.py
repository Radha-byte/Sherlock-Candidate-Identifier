from backend.meeting import MeetingSimulator
from backend.candidate_identifier import CandidateIdentifier

simulator = MeetingSimulator("data/meeting_data.json")

simulator.load_events()

identifier = CandidateIdentifier(simulator)

identifier.process_events()

best = identifier.get_best_candidate()

print("=" * 60)
print("BEST CANDIDATE")
print("=" * 60)

print("Display Name :", best.display_name)
print("Confidence   :", round(best.confidence, 2))

print("\nEvidence")

for evidence in best.evidence:
    print(f"- {evidence.reason} (+{evidence.score})")