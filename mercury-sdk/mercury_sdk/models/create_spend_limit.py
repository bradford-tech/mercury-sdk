from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.spend_limit_interval import SpendLimitInterval

T = TypeVar("T", bound="CreateSpendLimit")


@_attrs_define
class CreateSpendLimit:
    """
    Attributes:
        amount_cents (int):  Maximum total spend allowed per interval, in cents.
        interval (SpendLimitInterval):
    """

    amount_cents: int
    interval: SpendLimitInterval
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_cents = self.amount_cents

        interval = self.interval.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountCents": amount_cents,
                "interval": interval,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_cents = d.pop("amountCents")

        interval = SpendLimitInterval(d.pop("interval"))

        create_spend_limit = cls(
            amount_cents=amount_cents,
            interval=interval,
        )

        create_spend_limit.additional_properties = d
        return create_spend_limit

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
