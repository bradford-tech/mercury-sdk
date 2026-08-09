from enum import Enum


class ListSendMoneyApprovalRequestsStatus(str, Enum):
    APPROVED = "approved"
    CANCELLED = "cancelled"
    PENDINGAPPROVAL = "pendingApproval"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
