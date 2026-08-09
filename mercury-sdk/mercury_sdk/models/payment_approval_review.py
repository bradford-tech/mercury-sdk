from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_approval_review_status import PaymentApprovalReviewStatus

T = TypeVar("T", bound="PaymentApprovalReview")


@_attrs_define
class PaymentApprovalReview:
    """
    Attributes:
        reviewed_at (datetime.datetime):  Example: 2016-07-22T00:00:00Z.
        reviewer_user_id (UUID): ID for the user
        status (PaymentApprovalReviewStatus):
    """

    reviewed_at: datetime.datetime
    reviewer_user_id: UUID
    status: PaymentApprovalReviewStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reviewed_at = self.reviewed_at.isoformat()

        reviewer_user_id = str(self.reviewer_user_id)

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reviewedAt": reviewed_at,
                "reviewerUserId": reviewer_user_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reviewed_at = datetime.datetime.fromisoformat(d.pop("reviewedAt"))

        reviewer_user_id = UUID(d.pop("reviewerUserId"))

        status = PaymentApprovalReviewStatus(d.pop("status"))

        payment_approval_review = cls(
            reviewed_at=reviewed_at,
            reviewer_user_id=reviewer_user_id,
            status=status,
        )

        payment_approval_review.additional_properties = d
        return payment_approval_review

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
