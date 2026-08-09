from enum import Enum


class ApiOrganizationKind(str, Enum):
    BUSINESS = "business"
    PERSONAL = "personal"

    def __str__(self) -> str:
        return str(self.value)
