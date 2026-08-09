from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_send_money_payment_method import RequestSendMoneyPaymentMethod
from ..models.review_request_status import ReviewRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_approval_review import PaymentApprovalReview


T = TypeVar("T", bound="SendMoneyApprovalRequestResponse")


@_attrs_define
class SendMoneyApprovalRequestResponse:
    """A pending or completed approval request for a Mercury payment.

    Attributes:
        account_id (UUID): ID for a Mercury account.
        amount (float): A positive dollar amount with at least 1 cent.
        created_at (datetime.datetime):  Time at which the payment request was created. Example: 2016-07-22T00:00:00Z.
        payment_method (RequestSendMoneyPaymentMethod):
        recipient_id (UUID): ID for a Mercury account.
        request_id (str):
        requested_by_user_id (UUID):  The user who created the payment request.
        reviews (list[PaymentApprovalReview]):  Approval decisions recorded against this request, ordered from
             oldest to most recent.
        status (ReviewRequestStatus):
        memo (None | str | Unset):
        number_of_approvers_required (int | None | Unset):  Total number of approvals required for this payment to be
            sent.
             May be null for older requests where the requirement is not available.
        scheduled_send_date (datetime.date | None | Unset):  Date on which the payment is scheduled to be sent once
            fully
             approved. Null when the payment will be sent as soon as approvals
             are complete. Example: 2016-07-22.
    """

    account_id: UUID
    amount: float
    created_at: datetime.datetime
    payment_method: RequestSendMoneyPaymentMethod
    recipient_id: UUID
    request_id: str
    requested_by_user_id: UUID
    reviews: list[PaymentApprovalReview]
    status: ReviewRequestStatus
    memo: None | str | Unset = UNSET
    number_of_approvers_required: int | None | Unset = UNSET
    scheduled_send_date: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = str(self.account_id)

        amount = self.amount

        created_at = self.created_at.isoformat()

        payment_method = self.payment_method.value

        recipient_id = str(self.recipient_id)

        request_id = self.request_id

        requested_by_user_id = str(self.requested_by_user_id)

        reviews = []
        for reviews_item_data in self.reviews:
            reviews_item = reviews_item_data.to_dict()
            reviews.append(reviews_item)

        status = self.status.value

        memo: None | str | Unset
        if isinstance(self.memo, Unset):
            memo = UNSET
        else:
            memo = self.memo

        number_of_approvers_required: int | None | Unset
        if isinstance(self.number_of_approvers_required, Unset):
            number_of_approvers_required = UNSET
        else:
            number_of_approvers_required = self.number_of_approvers_required

        scheduled_send_date: None | str | Unset
        if isinstance(self.scheduled_send_date, Unset):
            scheduled_send_date = UNSET
        elif isinstance(self.scheduled_send_date, datetime.date):
            scheduled_send_date = self.scheduled_send_date.isoformat()
        else:
            scheduled_send_date = self.scheduled_send_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "amount": amount,
                "createdAt": created_at,
                "paymentMethod": payment_method,
                "recipientId": recipient_id,
                "requestId": request_id,
                "requestedByUserId": requested_by_user_id,
                "reviews": reviews,
                "status": status,
            }
        )
        if memo is not UNSET:
            field_dict["memo"] = memo
        if number_of_approvers_required is not UNSET:
            field_dict["numberOfApproversRequired"] = number_of_approvers_required
        if scheduled_send_date is not UNSET:
            field_dict["scheduledSendDate"] = scheduled_send_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_approval_review import PaymentApprovalReview

        d = dict(src_dict)
        account_id = UUID(d.pop("accountId"))

        amount = d.pop("amount")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        payment_method = RequestSendMoneyPaymentMethod(d.pop("paymentMethod"))

        recipient_id = UUID(d.pop("recipientId"))

        request_id = d.pop("requestId")

        requested_by_user_id = UUID(d.pop("requestedByUserId"))

        reviews = []
        _reviews = d.pop("reviews")
        for reviews_item_data in _reviews:
            reviews_item = PaymentApprovalReview.from_dict(reviews_item_data)

            reviews.append(reviews_item)

        status = ReviewRequestStatus(d.pop("status"))

        def _parse_memo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        memo = _parse_memo(d.pop("memo", UNSET))

        def _parse_number_of_approvers_required(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_approvers_required = _parse_number_of_approvers_required(d.pop("numberOfApproversRequired", UNSET))

        def _parse_scheduled_send_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_send_date_type_0 = datetime.date.fromisoformat(data)

                return scheduled_send_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        scheduled_send_date = _parse_scheduled_send_date(d.pop("scheduledSendDate", UNSET))

        send_money_approval_request_response = cls(
            account_id=account_id,
            amount=amount,
            created_at=created_at,
            payment_method=payment_method,
            recipient_id=recipient_id,
            request_id=request_id,
            requested_by_user_id=requested_by_user_id,
            reviews=reviews,
            status=status,
            memo=memo,
            number_of_approvers_required=number_of_approvers_required,
            scheduled_send_date=scheduled_send_date,
        )

        send_money_approval_request_response.additional_properties = d
        return send_money_approval_request_response

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
