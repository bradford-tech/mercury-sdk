from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiUpdateTransactionRequest")


@_attrs_define
class ApiUpdateTransactionRequest:
    """Request body for updating transaction metadata via the public API

    Attributes:
        category_id (UUID):  How to update the transaction's category. Omit field to keep current, send null to clear,
            send ID to set.
        note (None | str):  How to update the transaction's note. Omit field to keep current, send null/empty to clear,
            send text to set.
    """

    category_id: UUID
    note: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_id = str(self.category_id)

        note: None | str
        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "categoryId": category_id,
                "note": note,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_id = UUID(d.pop("categoryId"))

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        api_update_transaction_request = cls(
            category_id=category_id,
            note=note,
        )

        api_update_transaction_request.additional_properties = d
        return api_update_transaction_request

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
