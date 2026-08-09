from enum import Enum


class APIApplicationType(str, Enum):
    DEFAULTAPPLICATION = "DefaultApplication"
    PENDINGEINAPPLICATION = "PendingEINApplication"

    def __str__(self) -> str:
        return str(self.value)
