from enum import Enum


class PostTransactionPaymentMethod(str, Enum):
    ACH = "ach"
    CHECK = "check"
    DOMESTICWIRE = "domesticWire"

    def __str__(self) -> str:
        return str(self.value)
