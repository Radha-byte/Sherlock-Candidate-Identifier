from dataclasses import dataclass


@dataclass
class MeetingEvent:

    timestamp: int

    event_type: str

    participant_id: str

    text: str = ""

    display_name: str = ""

    duration: float = 0.0