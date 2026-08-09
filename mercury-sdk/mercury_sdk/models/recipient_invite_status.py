from enum import Enum


class RecipientInviteStatus(str, Enum):
    COMPLETED = "completed"
    CREATED = "created"
    EXPIRED = "expired"

    def __str__(self) -> str:
        return str(self.value)
