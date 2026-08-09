from enum import Enum


class CitizenshipStatus(str, Enum):
    NONRESIDENT = "NonResident"
    USCITIZEN = "USCitizen"
    USRESIDENT = "USResident"

    def __str__(self) -> str:
        return str(self.value)
