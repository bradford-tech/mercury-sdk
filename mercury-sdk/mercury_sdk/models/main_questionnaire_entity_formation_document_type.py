from enum import Enum


class MainQuestionnaireEntityFormationDocumentType(str, Enum):
    ARTICLESOFINCORPORATION = "ArticlesOfIncorporation"
    ARTICLESOFORGANIZATION = "ArticlesOfOrganization"
    CERTIFICATEOFFORMATION = "CertificateOfFormation"
    PARTNERSHIPAGREEMENT = "PartnershipAgreement"
    SECRETARYOFSTATEREGISTRATIONPAGE = "SecretaryOfStateRegistrationPage"

    def __str__(self) -> str:
        return str(self.value)
