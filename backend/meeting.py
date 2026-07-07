import json

from backend.event_models import MeetingEvent


class MeetingSimulator:

    def __init__(self, meeting_file: str):
        self.meeting_file = meeting_file
        self.events = []

    def load_events(self):

        with open(self.meeting_file, "r") as file:

            data = json.load(file)

        for event in data["events"]:

            self.events.append(
                MeetingEvent(
                    timestamp=event["timestamp"],
                    event_type=event["type"],
                    participant_id=event["participant_id"],
                    text=event.get("text", ""),
                    display_name=event.get("display_name", "")
                )
            )

    def get_events(self):

        return sorted(self.events, key=lambda x: x.timestamp)