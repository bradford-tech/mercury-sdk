from enum import Enum


class SafeRequestInvestorType(str, Enum):
    SAFEREQUESTINVESTORTYPEINDIVIDUAL = "SafeRequestInvestorTypeIndividual"
    SAFEREQUESTINVESTORTYPEOTHER = "SafeRequestInvestorTypeOther"
    SAFEREQUESTINVESTORTYPEVENTUREFUND = "SafeRequestInvestorTypeVentureFund"

    def __str__(self) -> str:
        return str(self.value)
