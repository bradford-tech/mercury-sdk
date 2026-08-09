from enum import Enum


class GetWebhooksStatusItem(str, Enum):
    ACTIVE = "active"
    DELETED = "deleted"
    DISABLED = "disabled"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
