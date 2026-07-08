import json

from backend.event_models import MeetingEvent
from backend.participant_manager import ParticipantManager


class MeetingSimulator:

    def __init__(self, meeting_file: str):

        self.meeting_file = meeting_file

        self.events = []

        self.manager = ParticipantManager()

    def load_events(self):

        with open(self.meeting_file, "r") as file:

            data = json.load(file)

        for event in data["events"]:

            meeting_event = MeetingEvent(
                timestamp=event["timestamp"],
                event_type=event["type"],
                participant_id=event["participant_id"],
                text=event.get("text", ""),
                display_name=event.get("display_name", "")
            )

            self.events.append(meeting_event)

            if meeting_event.event_type == "participant_join":

                self.manager.add_participant(
                    meeting_event.participant_id,
                    meeting_event.display_name
                )

    def get_events(self):

        return sorted(self.events, key=lambda x: x.timestamp)

    def get_participants(self):

        return self.manager.get_all_participants()