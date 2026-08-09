from enum import Enum


class ListTransactionsStatusItem(str, Enum):
    BLOCKED = "blocked"
    CANCELLED = "cancelled"
    FAILED = "failed"
    PENDING = "pending"
    REVERSED = "reversed"
    SENT = "sent"

    def __str__(self) -> str:
        return str(self.value)
