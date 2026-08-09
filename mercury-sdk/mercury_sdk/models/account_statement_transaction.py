from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountStatementTransaction")


@_attrs_define
class AccountStatementTransaction:
    """
    Attributes:
        created_at (datetime.datetime):  Example: 2016-07-22T00:00:00Z.
        id (UUID): ID for this transaction
        posted_at (datetime.datetime | None | Unset):  Example: 2016-07-22T00:00:00Z.
    """

    created_at: datetime.datetime
    id: UUID
    posted_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = str(self.id)

        posted_at: None | str | Unset
        if isinstance(self.posted_at, Unset):
            posted_at = UNSET
        elif isinstance(self.posted_at, datetime.datetime):
            posted_at = self.posted_at.isoformat()
        else:
            posted_at = self.posted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
            }
        )
        if posted_at is not UNSET:
            field_dict["postedAt"] = posted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        id = UUID(d.pop("id"))

        def _parse_posted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                posted_at_type_0 = datetime.datetime.fromisoformat(data)

                return posted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        posted_at = _parse_posted_at(d.pop("postedAt", UNSET))

        account_statement_transaction = cls(
            created_at=created_at,
            id=id,
            posted_at=posted_at,
        )

        account_statement_transaction.additional_properties = d
        return account_statement_transaction

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
