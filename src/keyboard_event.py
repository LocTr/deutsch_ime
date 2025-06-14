from enum import Enum , auto
from dataclasses import dataclass


class EventType(Enum):
    KEY_PRESS = auto()
    KEY_RELEASE = auto()


@dataclass(frozen=True)
class KeyEvent:

    key: str
    event_type: EventType