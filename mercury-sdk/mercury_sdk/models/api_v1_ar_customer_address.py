from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiV1ArCustomerAddress")


@_attrs_define
class ApiV1ArCustomerAddress:
    """Customer address information for Accounts Receivable API

    Attributes:
        address1 (str):  Primary street address line.
        city (str):  City name.
        country (str):  Two-letter country code (ISO 3166-1 alpha-2).
        postal_code (str):  Postal or ZIP code
        region (str):  State, province, or region.
        address2 (None | str | Unset):  Secondary street address line (optional).
    """

    address1: str
    city: str
    country: str
    postal_code: str
    region: str
    address2: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address1 = self.address1

        city = self.city

        country = self.country

        postal_code = self.postal_code

        region = self.region

        address2: None | str | Unset
        if isinstance(self.address2, Unset):
            address2 = UNSET
        else:
            address2 = self.address2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address1": address1,
                "city": city,
                "country": country,
                "postalCode": postal_code,
                "region": region,
            }
        )
        if address2 is not UNSET:
            field_dict["address2"] = address2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address1 = d.pop("address1")

        city = d.pop("city")

        country = d.pop("country")

        postal_code = d.pop("postalCode")

        region = d.pop("region")

        def _parse_address2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address2 = _parse_address2(d.pop("address2", UNSET))

        api_v1_ar_customer_address = cls(
            address1=address1,
            city=city,
            country=country,
            postal_code=postal_code,
            region=region,
            address2=address2,
        )

        api_v1_ar_customer_address.additional_properties = d
        return api_v1_ar_customer_address

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
