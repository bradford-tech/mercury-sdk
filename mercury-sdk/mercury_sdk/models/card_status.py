from enum import Enum


class CardStatus(str, Enum):
    ACTIVE = "active"
    CANCELLED = "cancelled"
    EXPIRED = "expired"
    FROZEN = "frozen"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
