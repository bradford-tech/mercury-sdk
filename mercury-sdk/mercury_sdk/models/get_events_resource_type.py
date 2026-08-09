from enum import Enum


class GetEventsResourceType(str, Enum):
    CHECKINGACCOUNT = "checkingAccount"
    CREDITACCOUNT = "creditAccount"
    INVESTMENTACCOUNT = "investmentAccount"
    SAVINGSACCOUNT = "savingsAccount"
    TRANSACTION = "transaction"
    TREASURYACCOUNT = "treasuryAccount"

    def __str__(self) -> str:
        return str(self.value)
