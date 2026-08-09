from enum import Enum


class BeneficialOwnerJobTitle(str, Enum):
    CHIEFEXECUTIVEOFFICER = "ChiefExecutiveOfficer"
    CHIEFFINANCIALOFFICER = "ChiefFinancialOfficer"
    CHIEFOPERATINGOFFICER = "ChiefOperatingOfficer"
    CHIEFTECHNOLOGYOFFICER = "ChiefTechnologyOfficer"
    FINANCETEAM = "FinanceTeam"
    FOUNDER = "Founder"
    GENERALPARTNER = "GeneralPartner"
    OTHER = "Other"
    PRESIDENT = "President"

    def __str__(self) -> str:
        return str(self.value)
