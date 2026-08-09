from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalTransferAPIRequest")


@_attrs_define
class InternalTransferAPIRequest:
    """Request body for POST /api/v1/transfer endpoint.
    Transfers funds between two depository, treasury, or investment accounts belonging to the same organization.

       Attributes:
           amount (float): A positive dollar amount with at least 1 cent.
           destination_account_id (UUID): ID for a Mercury account.
           idempotency_key (str):
           source_account_id (UUID): ID for a Mercury account.
           note (None | str | Unset):
    """

    amount: float
    destination_account_id: UUID
    idempotency_key: str
    source_account_id: UUID
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        destination_account_id = str(self.destination_account_id)

        idempotency_key = self.idempotency_key

        source_account_id = str(self.source_account_id)

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "destinationAccountId": destination_account_id,
                "idempotencyKey": idempotency_key,
                "sourceAccountId": source_account_id,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        destination_account_id = UUID(d.pop("destinationAccountId"))

        idempotency_key = d.pop("idempotencyKey")

        source_account_id = UUID(d.pop("sourceAccountId"))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        internal_transfer_api_request = cls(
            amount=amount,
            destination_account_id=destination_account_id,
            idempotency_key=idempotency_key,
            source_account_id=source_account_id,
            note=note,
        )

        internal_transfer_api_request.additional_properties = d
        return internal_transfer_api_request

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
