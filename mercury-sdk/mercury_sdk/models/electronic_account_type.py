from enum import Enum


class ElectronicAccountType(str, Enum):
    BUSINESSCHECKING = "businessChecking"
    BUSINESSSAVINGS = "businessSavings"
    PERSONALCHECKING = "personalChecking"
    PERSONALSAVINGS = "personalSavings"

    def __str__(self) -> str:
        return str(self.value)
