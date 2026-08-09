from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.treasury_net_return_status import TreasuryNetReturnStatus

if TYPE_CHECKING:
    from ..models.treasury_dividend import TreasuryDividend


T = TypeVar("T", bound="TreasuryNetReturn")


@_attrs_define
class TreasuryNetReturn:
    """Monthly net return breakdown for a treasury account

    Attributes:
        dividends (list[TreasuryDividend]):  List of dividends received by security
        month (datetime.date):  First day of the month for this net return Example: 2016-07-22.
        net_amount (float):  Net return amount (dividends minus fees)
        status (TreasuryNetReturnStatus):
        treasury_fee (float):  Treasury fee charged for this period (positive value)
    """

    dividends: list[TreasuryDividend]
    month: datetime.date
    net_amount: float
    status: TreasuryNetReturnStatus
    treasury_fee: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dividends = []
        for dividends_item_data in self.dividends:
            dividends_item = dividends_item_data.to_dict()
            dividends.append(dividends_item)

        month = self.month.isoformat()

        net_amount = self.net_amount

        status = self.status.value

        treasury_fee = self.treasury_fee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dividends": dividends,
                "month": month,
                "netAmount": net_amount,
                "status": status,
                "treasuryFee": treasury_fee,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.treasury_dividend import TreasuryDividend

        d = dict(src_dict)
        dividends = []
        _dividends = d.pop("dividends")
        for dividends_item_data in _dividends:
            dividends_item = TreasuryDividend.from_dict(dividends_item_data)

            dividends.append(dividends_item)

        month = datetime.date.fromisoformat(d.pop("month"))

        net_amount = d.pop("netAmount")

        status = TreasuryNetReturnStatus(d.pop("status"))

        treasury_fee = d.pop("treasuryFee")

        treasury_net_return = cls(
            dividends=dividends,
            month=month,
            net_amount=net_amount,
            status=status,
            treasury_fee=treasury_fee,
        )

        treasury_net_return.additional_properties = d
        return treasury_net_return

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
