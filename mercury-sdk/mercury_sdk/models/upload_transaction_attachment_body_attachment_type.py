from enum import Enum


class UploadTransactionAttachmentBodyAttachmentType(str, Enum):
    BILL = "bill"
    OTHER = "other"
    RECEIPT = "receipt"

    def __str__(self) -> str:
        return str(self.value)
