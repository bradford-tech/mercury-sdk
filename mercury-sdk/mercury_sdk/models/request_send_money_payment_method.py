from enum import Enum


class RequestSendMoneyPaymentMethod(str, Enum):
    ACH = "ach"
    CHECK = "check"
    DOMESTICWIRE = "domesticWire"
    INTERNATIONALWIRE = "internationalWire"

    def __str__(self) -> str:
        return str(self.value)
