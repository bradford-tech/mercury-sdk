from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_status import AccountStatus

T = TypeVar("T", bound="CreditAccount")


@_attrs_define
class CreditAccount:
    """
    Attributes:
        available_balance (float):
        created_at (datetime.datetime):  Example: 2016-07-22T00:00:00Z.
        current_balance (float):
        id (UUID): ID for a Mercury account.
        status (AccountStatus):
    """

    available_balance: float
    created_at: datetime.datetime
    current_balance: float
    id: UUID
    status: AccountStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_balance = self.available_balance

        created_at = self.created_at.isoformat()

        current_balance = self.current_balance

        id = str(self.id)

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "availableBalance": available_balance,
                "createdAt": created_at,
                "currentBalance": current_balance,
                "id": id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available_balance = d.pop("availableBalance")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        current_balance = d.pop("currentBalance")

        id = UUID(d.pop("id"))

        status = AccountStatus(d.pop("status"))

        credit_account = cls(
            available_balance=available_balance,
            created_at=created_at,
            current_balance=current_balance,
            id=id,
            status=status,
        )

        credit_account.additional_properties = d
        return credit_account

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
