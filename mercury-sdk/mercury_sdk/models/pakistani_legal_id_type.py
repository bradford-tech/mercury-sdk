from enum import Enum


class PakistaniLegalIdType(str, Enum):
    CNIC = "CNIC"
    NTN = "NTN"
    PASSPORT = "Passport"
    SNIC = "SNIC"

    def __str__(self) -> str:
        return str(self.value)
