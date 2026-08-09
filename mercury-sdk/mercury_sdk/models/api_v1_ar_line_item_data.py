from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiV1ArLineItemData")


@_attrs_define
class ApiV1ArLineItemData:
    """Data for an invoice line item

    Attributes:
        name (str):  the name of the line item
        quantity (float):  the quantity of this item
        unit_price (float):  the price of one unit of the item before sales tax
        sales_tax_rate (float | None | Unset):  the sales tax applied to this item
    """

    name: str
    quantity: float
    unit_price: float
    sales_tax_rate: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        quantity = self.quantity

        unit_price = self.unit_price

        sales_tax_rate: float | None | Unset
        if isinstance(self.sales_tax_rate, Unset):
            sales_tax_rate = UNSET
        else:
            sales_tax_rate = self.sales_tax_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "quantity": quantity,
                "unitPrice": unit_price,
            }
        )
        if sales_tax_rate is not UNSET:
            field_dict["salesTaxRate"] = sales_tax_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        quantity = d.pop("quantity")

        unit_price = d.pop("unitPrice")

        def _parse_sales_tax_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sales_tax_rate = _parse_sales_tax_rate(d.pop("salesTaxRate", UNSET))

        api_v1_ar_line_item_data = cls(
            name=name,
            quantity=quantity,
            unit_price=unit_price,
            sales_tax_rate=sales_tax_rate,
        )

        api_v1_ar_line_item_data.additional_properties = d
        return api_v1_ar_line_item_data

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
