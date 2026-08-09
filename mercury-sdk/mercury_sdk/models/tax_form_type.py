from enum import Enum


class TaxFormType(str, Enum):
    UNKNOWN = "unknown"
    W8BEN = "w8BEN"
    W8BENE = "w8BENE"
    W9 = "w9"

    def __str__(self) -> str:
        return str(self.value)
