from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.spend_limit_interval import SpendLimitInterval
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpendLimit")


@_attrs_define
class SpendLimit:
    """Spending controls applied to a card

    Attributes:
        amount_cents (int):  Maximum total spend allowed per interval, in cents.
        interval (SpendLimitInterval):
        atm_amount_cents (int | None | Unset):  Maximum ATM withdrawal allowed per interval, in cents. Null for virtual
            cards.
    """

    amount_cents: int
    interval: SpendLimitInterval
    atm_amount_cents: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_cents = self.amount_cents

        interval = self.interval.value

        atm_amount_cents: int | None | Unset
        if isinstance(self.atm_amount_cents, Unset):
            atm_amount_cents = UNSET
        else:
            atm_amount_cents = self.atm_amount_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountCents": amount_cents,
                "interval": interval,
            }
        )
        if atm_amount_cents is not UNSET:
            field_dict["atmAmountCents"] = atm_amount_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_cents = d.pop("amountCents")

        interval = SpendLimitInterval(d.pop("interval"))

        def _parse_atm_amount_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        atm_amount_cents = _parse_atm_amount_cents(d.pop("atmAmountCents", UNSET))

        spend_limit = cls(
            amount_cents=amount_cents,
            interval=interval,
            atm_amount_cents=atm_amount_cents,
        )

        spend_limit.additional_properties = d
        return spend_limit

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
