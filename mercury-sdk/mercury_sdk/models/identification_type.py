from enum import Enum


class IdentificationType(str, Enum):
    ALIENREGISTRATIONCARD = "AlienRegistrationCard"
    DRIVERSLICENSE = "DriversLicense"
    EMPLOYEEAUTHORIZATIONDOCUMENT = "EmployeeAuthorizationDocument"
    NATIONALID = "NationalID"
    PASSPORT = "Passport"
    RESIDENCEPERMIT = "ResidencePermit"
    STATEID = "StateID"
    VERIFIEDBYTHIRDPARTY = "VerifiedByThirdParty"
    VISA = "Visa"

    def __str__(self) -> str:
        return str(self.value)
