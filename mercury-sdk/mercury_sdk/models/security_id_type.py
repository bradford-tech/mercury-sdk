from enum import Enum


class SecurityIdType(str, Enum):
    CUSIP = "cusip"

    def __str__(self) -> str:
        return str(self.value)
