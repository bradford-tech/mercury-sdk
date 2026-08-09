from enum import Enum


class CardNetwork(str, Enum):
    MASTERCARD = "mastercard"
    VISA = "visa"

    def __str__(self) -> str:
        return str(self.value)
