from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_status import AccountStatus

if TYPE_CHECKING:
    from ..models.treasury_net_return import TreasuryNetReturn


T = TypeVar("T", bound="TreasuryAccount")


@_attrs_define
class TreasuryAccount:
    """
    Attributes:
        available_balance (float):
        created_at (datetime.datetime):  Example: 2016-07-22T00:00:00Z.
        current_balance (float):
        id (UUID): ID for a Mercury account.
        net_returns (list[TreasuryNetReturn]):  Monthly net return breakdown with dividend and fee details
        status (AccountStatus):
    """

    available_balance: float
    created_at: datetime.datetime
    current_balance: float
    id: UUID
    net_returns: list[TreasuryNetReturn]
    status: AccountStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_balance = self.available_balance

        created_at = self.created_at.isoformat()

        current_balance = self.current_balance

        id = str(self.id)

        net_returns = []
        for net_returns_item_data in self.net_returns:
            net_returns_item = net_returns_item_data.to_dict()
            net_returns.append(net_returns_item)

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "availableBalance": available_balance,
                "createdAt": created_at,
                "currentBalance": current_balance,
                "id": id,
                "netReturns": net_returns,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.treasury_net_return import TreasuryNetReturn

        d = dict(src_dict)
        available_balance = d.pop("availableBalance")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        current_balance = d.pop("currentBalance")

        id = UUID(d.pop("id"))

        net_returns = []
        _net_returns = d.pop("netReturns")
        for net_returns_item_data in _net_returns:
            net_returns_item = TreasuryNetReturn.from_dict(net_returns_item_data)

            net_returns.append(net_returns_item)

        status = AccountStatus(d.pop("status"))

        treasury_account = cls(
            available_balance=available_balance,
            created_at=created_at,
            current_balance=current_balance,
            id=id,
            net_returns=net_returns,
            status=status,
        )

        treasury_account.additional_properties = d
        return treasury_account

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
