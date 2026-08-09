from enum import Enum


class PaymentMethod(str, Enum):
    ACH = "ach"
    CHECK = "check"
    DOMESTICWIRE = "domesticWire"
    INTERNATIONALWIRE = "internationalWire"
    REALTIMEPAYMENT = "realTimePayment"

    def __str__(self) -> str:
        return str(self.value)
