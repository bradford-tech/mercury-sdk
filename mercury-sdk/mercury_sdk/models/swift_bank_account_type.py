from enum import Enum


class SwiftBankAccountType(str, Enum):
    CHECKING = "checking"
    SAVINGS = "savings"

    def __str__(self) -> str:
        return str(self.value)
