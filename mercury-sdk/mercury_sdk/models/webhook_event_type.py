from enum import Enum


class WebhookEventType(str, Enum):
    CHECKINGACCOUNT_BALANCE_UPDATED = "checkingAccount.balance.updated"
    CREDITACCOUNT_BALANCE_UPDATED = "creditAccount.balance.updated"
    INVESTMENTACCOUNT_BALANCE_UPDATED = "investmentAccount.balance.updated"
    SAVINGSACCOUNT_BALANCE_UPDATED = "savingsAccount.balance.updated"
    TRANSACTION_CREATED = "transaction.created"
    TRANSACTION_UPDATED = "transaction.updated"
    TREASURYACCOUNT_BALANCE_UPDATED = "treasuryAccount.balance.updated"

    def __str__(self) -> str:
        return str(self.value)
