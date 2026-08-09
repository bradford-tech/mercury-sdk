from enum import Enum


class ListRecipientInvitesStatus(str, Enum):
    COMPLETED = "completed"
    CREATED = "created"
    EXPIRED = "expired"

    def __str__(self) -> str:
        return str(self.value)
