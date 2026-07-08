from backend.meeting import MeetingSimulator

simulator = MeetingSimulator("data/meeting_data.json")

simulator.load_events()

print("Meeting Events")

print("-" * 50)

for event in simulator.get_events():

    print(event)

print()

print("Participants")

print("-" * 50)

for participant in simulator.get_participants():

    print(participant)