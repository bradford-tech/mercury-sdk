from enum import Enum


class TransactionAttachmentType(str, Enum):
    CHECKIMAGE = "checkImage"
    OTHER = "other"
    RECEIPT = "receipt"

    def __str__(self) -> str:
        return str(self.value)
