from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_send_money_payment_method import RequestSendMoneyPaymentMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_transaction_send_money_purpose import PostTransactionSendMoneyPurpose


T = TypeVar("T", bound="SendMoneyAPIRequest")


@_attrs_define
class SendMoneyAPIRequest:
    """
    Attributes:
        amount (float): Amount of USD you want to send, must be a positive number.
        idempotency_key (str): Unique string identifying the transaction
        payment_method (RequestSendMoneyPaymentMethod):
        recipient_id (UUID): Recipient ID from the /recipients endpoint.
        external_memo (str | Unset): Optional external memo
        note (str | Unset): Optional note
        purpose (PostTransactionSendMoneyPurpose | Unset):  External API representation of SendMoneyPurpose.
             Only exposes the 'simple' field to decouple internal implementation from external API.
    """

    amount: float
    idempotency_key: str
    payment_method: RequestSendMoneyPaymentMethod
    recipient_id: UUID
    external_memo: str | Unset = UNSET
    note: str | Unset = UNSET
    purpose: PostTransactionSendMoneyPurpose | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        idempotency_key = self.idempotency_key

        payment_method = self.payment_method.value

        recipient_id = str(self.recipient_id)

        external_memo = self.external_memo

        note = self.note

        purpose: dict[str, Any] | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "idempotencyKey": idempotency_key,
                "paymentMethod": payment_method,
                "recipientId": recipient_id,
            }
        )
        if external_memo is not UNSET:
            field_dict["externalMemo"] = external_memo
        if note is not UNSET:
            field_dict["note"] = note
        if purpose is not UNSET:
            field_dict["purpose"] = purpose

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_transaction_send_money_purpose import PostTransactionSendMoneyPurpose

        d = dict(src_dict)
        amount = d.pop("amount")

        idempotency_key = d.pop("idempotencyKey")

        payment_method = RequestSendMoneyPaymentMethod(d.pop("paymentMethod"))

        recipient_id = UUID(d.pop("recipientId"))

        external_memo = d.pop("externalMemo", UNSET)

        note = d.pop("note", UNSET)

        _purpose = d.pop("purpose", UNSET)
        purpose: PostTransactionSendMoneyPurpose | Unset
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = PostTransactionSendMoneyPurpose.from_dict(_purpose)

        send_money_api_request = cls(
            amount=amount,
            idempotency_key=idempotency_key,
            payment_method=payment_method,
            recipient_id=recipient_id,
            external_memo=external_memo,
            note=note,
            purpose=purpose,
        )

        send_money_api_request.additional_properties = d
        return send_money_api_request

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
