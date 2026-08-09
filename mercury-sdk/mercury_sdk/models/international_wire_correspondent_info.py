from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternationalWireCorrespondentInfo")


@_attrs_define
class InternationalWireCorrespondentInfo:
    """
    Attributes:
        bank_name (None | str | Unset):
        routing_number (None | str | Unset):
        swift_code (None | str | Unset):
    """

    bank_name: None | str | Unset = UNSET
    routing_number: None | str | Unset = UNSET
    swift_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bank_name: None | str | Unset
        if isinstance(self.bank_name, Unset):
            bank_name = UNSET
        else:
            bank_name = self.bank_name

        routing_number: None | str | Unset
        if isinstance(self.routing_number, Unset):
            routing_number = UNSET
        else:
            routing_number = self.routing_number

        swift_code: None | str | Unset
        if isinstance(self.swift_code, Unset):
            swift_code = UNSET
        else:
            swift_code = self.swift_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bank_name is not UNSET:
            field_dict["bankName"] = bank_name
        if routing_number is not UNSET:
            field_dict["routingNumber"] = routing_number
        if swift_code is not UNSET:
            field_dict["swiftCode"] = swift_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_bank_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_name = _parse_bank_name(d.pop("bankName", UNSET))

        def _parse_routing_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        routing_number = _parse_routing_number(d.pop("routingNumber", UNSET))

        def _parse_swift_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        swift_code = _parse_swift_code(d.pop("swiftCode", UNSET))

        international_wire_correspondent_info = cls(
            bank_name=bank_name,
            routing_number=routing_number,
            swift_code=swift_code,
        )

        international_wire_correspondent_info.additional_properties = d
        return international_wire_correspondent_info

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
