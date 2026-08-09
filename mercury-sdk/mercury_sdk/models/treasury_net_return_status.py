from enum import Enum


class TreasuryNetReturnStatus(str, Enum):
    CHARGED = "charged"
    ERROR = "error"
    PENDING = "pending"
    PROCESSING = "processing"

    def __str__(self) -> str:
        return str(self.value)
