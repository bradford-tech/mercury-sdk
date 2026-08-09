from enum import Enum


class ApiUserRole(str, Enum):
    ADMINISTRATOR = "administrator"
    BOOKKEEPER = "bookkeeper"
    CARDONLYUSER = "cardOnlyUser"
    CUSTOMUSER = "customUser"
    EMPLOYEE = "employee"

    def __str__(self) -> str:
        return str(self.value)
