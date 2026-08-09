from enum import Enum


class CreateCardType(str, Enum):
    VIRTUAL = "virtual"

    def __str__(self) -> str:
        return str(self.value)
