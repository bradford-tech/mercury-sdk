from enum import Enum


class CardType(str, Enum):
    PHYSICAL = "physical"
    VIRTUAL = "virtual"

    def __str__(self) -> str:
        return str(self.value)
