from enum import Enum


class PaymentLinkStatus(str, Enum):
    CANCELLED = "Cancelled"
    PAID = "Paid"
    PROCESSING = "Processing"
    UNPAID = "Unpaid"

    def __str__(self) -> str:
        return str(self.value)
