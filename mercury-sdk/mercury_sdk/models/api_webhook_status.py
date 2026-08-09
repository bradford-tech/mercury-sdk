from enum import Enum


class ApiWebhookStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
