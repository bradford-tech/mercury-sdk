from enum import Enum


class AccountStatus(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
