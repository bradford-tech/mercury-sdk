from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SwiftCodeData")


@_attrs_define
class SwiftCodeData:
    """
    Attributes:
        bank_city_state (str):
        bank_country (str):
        bank_name (str):
    """

    bank_city_state: str
    bank_country: str
    bank_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bank_city_state = self.bank_city_state

        bank_country = self.bank_country

        bank_name = self.bank_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bankCityState": bank_city_state,
                "bankCountry": bank_country,
                "bankName": bank_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bank_city_state = d.pop("bankCityState")

        bank_country = d.pop("bankCountry")

        bank_name = d.pop("bankName")

        swift_code_data = cls(
            bank_city_state=bank_city_state,
            bank_country=bank_country,
            bank_name=bank_name,
        )

        swift_code_data.additional_properties = d
        return swift_code_data

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
