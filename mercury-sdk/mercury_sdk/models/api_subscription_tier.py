from enum import Enum


class ApiSubscriptionTier(str, Enum):
    ENTERPRISE = "enterprise"
    FREE = "free"
    PLUS = "plus"
    PREMIUM = "premium"
    PRO = "pro"

    def __str__(self) -> str:
        return str(self.value)
