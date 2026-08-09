from enum import Enum


class SimplePurposeCategory(str, Enum):
    ANGELINVESTMENT = "angelInvestment"
    CONTRACTOR = "contractor"
    EMPLOYEE = "employee"
    EXPENSES = "expenses"
    FAMILYMEMBERORFRIEND = "familyMemberOrFriend"
    FORGOODSORSERVICES = "forGoodsOrServices"
    LANDLORD = "landlord"
    OTHER = "other"
    SAVINGSORINVESTMENTS = "savingsOrInvestments"
    SUBSIDIARY = "subsidiary"
    TRANSFERTOMYEXTERNALACCOUNT = "transferToMyExternalAccount"
    TRAVEL = "travel"
    VENDOR = "vendor"

    def __str__(self) -> str:
        return str(self.value)
