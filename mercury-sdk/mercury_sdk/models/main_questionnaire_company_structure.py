from enum import Enum


class MainQuestionnaireCompanyStructure(str, Enum):
    CCORP = "CCorp"
    EXEMPTEDCOMPANY = "ExemptedCompany"
    GENERALPARTNERSHIP = "GeneralPartnership"
    JOINTVENTURE = "JointVenture"
    LIMITED = "Limited"
    LIMITEDPARTNERSHIP = "LimitedPartnership"
    LLC = "LLC"
    LLCTAXEDASSOLEPROPRIETORSHIP = "LLCTaxedAsSoleProprietorship"
    LLP = "LLP"
    NONPROFIT = "NonProfit"
    PARTNERSHIP = "Partnership"
    PROFESSIONALASSOCIATION = "ProfessionalAssociation"
    PROFESSIONALCORPORATION = "ProfessionalCorporation"
    SCORP = "SCorp"
    SOLEPROPRIETORSHIP = "SoleProprietorship"

    def __str__(self) -> str:
        return str(self.value)
