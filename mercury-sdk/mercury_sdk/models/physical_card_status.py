from enum import Enum


class PhysicalCardStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    LOCKED = "locked"

    def __str__(self) -> str:
        return str(self.value)
