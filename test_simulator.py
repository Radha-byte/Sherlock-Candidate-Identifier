from backend.meeting import MeetingSimulator

simulator = MeetingSimulator("data/meeting_data.json")

simulator.load_events()

for event in simulator.get_events():
    print(event)