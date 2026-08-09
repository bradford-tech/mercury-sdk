from enum import Enum


class ResourceField(str, Enum):
    CHECKINGACCOUNT_AVAILABLEBALANCE = "checkingAccount.availableBalance"
    CHECKINGACCOUNT_CURRENTBALANCE = "checkingAccount.currentBalance"
    CHECKINGACCOUNT_INFLIGHTBALANCE = "checkingAccount.inFlightBalance"
    CREDITACCOUNT_AVAILABLEBALANCE = "creditAccount.availableBalance"
    CREDITACCOUNT_CURRENTBALANCE = "creditAccount.currentBalance"
    CREDITACCOUNT_INFLIGHTBALANCE = "creditAccount.inFlightBalance"
    INVESTMENTACCOUNT_AVAILABLEBALANCE = "investmentAccount.availableBalance"
    INVESTMENTACCOUNT_CURRENTBALANCE = "investmentAccount.currentBalance"
    INVESTMENTACCOUNT_INFLIGHTBALANCE = "investmentAccount.inFlightBalance"
    SAVINGSACCOUNT_AVAILABLEBALANCE = "savingsAccount.availableBalance"
    SAVINGSACCOUNT_CURRENTBALANCE = "savingsAccount.currentBalance"
    SAVINGSACCOUNT_INFLIGHTBALANCE = "savingsAccount.inFlightBalance"
    TRANSACTION_AMOUNT = "transaction.amount"
    TRANSACTION_BANKDESCRIPTION = "transaction.bankDescription"
    TRANSACTION_CATEGORYDATA = "transaction.categoryData"
    TRANSACTION_CUSTOMCATEGORY = "transaction.customCategory"
    TRANSACTION_CUSTOMCATEGORY_ID = "transaction.customCategory.id"
    TRANSACTION_CUSTOMCATEGORY_NAME = "transaction.customCategory.name"
    TRANSACTION_ESTIMATEDDELIVERYDATE = "transaction.estimatedDeliveryDate"
    TRANSACTION_EXTERNALMEMO = "transaction.externalMemo"
    TRANSACTION_FAILEDAT = "transaction.failedAt"
    TRANSACTION_MERCURYCATEGORY = "transaction.mercuryCategory"
    TRANSACTION_NOTE = "transaction.note"
    TRANSACTION_POSTEDAT = "transaction.postedAt"
    TRANSACTION_REASONFORFAILURE = "transaction.reasonForFailure"
    TRANSACTION_STATUS = "transaction.status"
    TREASURYACCOUNT_AVAILABLEBALANCE = "treasuryAccount.availableBalance"
    TREASURYACCOUNT_CURRENTBALANCE = "treasuryAccount.currentBalance"
    TREASURYACCOUNT_INFLIGHTBALANCE = "treasuryAccount.inFlightBalance"

    def __str__(self) -> str:
        return str(self.value)
