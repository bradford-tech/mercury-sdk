from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.security_id_type import SecurityIdType

T = TypeVar("T", bound="TreasuryDividend")


@_attrs_define
class TreasuryDividend:
    """Dividend information for a specific treasury security

    Attributes:
        amount (float):  Dividend amount for this security
        id (str):  Security identifier (e.g., "617455696")
        security_name (str):  Human-readable security name (e.g., "Morgan Stanley Ultra-Short Income Portfolio Class
            IR")
        type_ (SecurityIdType):
    """

    amount: float
    id: str
    security_name: str
    type_: SecurityIdType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        id = self.id

        security_name = self.security_name

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "id": id,
                "securityName": security_name,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        id = d.pop("id")

        security_name = d.pop("securityName")

        type_ = SecurityIdType(d.pop("type"))

        treasury_dividend = cls(
            amount=amount,
            id=id,
            security_name=security_name,
            type_=type_,
        )

        treasury_dividend.additional_properties = d
        return treasury_dividend

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
