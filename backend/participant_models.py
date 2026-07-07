from dataclasses import dataclass, field
from typing import List


@dataclass
class Evidence:
    source: str
    score: float
    reason: str


@dataclass
class Participant:

    participant_id: str

    display_name: str

    email: str = ""

    camera_on: bool = False

    microphone_on: bool = False

    speaking_duration: float = 0.0

    transcript: List[str] = field(default_factory=list)

    evidence: List[Evidence] = field(default_factory=list)

    confidence: float = 0.0