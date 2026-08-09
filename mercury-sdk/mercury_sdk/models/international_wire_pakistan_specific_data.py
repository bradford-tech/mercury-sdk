from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pakistani_legal_id_type import PakistaniLegalIdType

T = TypeVar("T", bound="InternationalWirePakistanSpecificData")


@_attrs_define
class InternationalWirePakistanSpecificData:
    """
    Attributes:
        legal_id (str):
        legal_id_type (PakistaniLegalIdType):
    """

    legal_id: str
    legal_id_type: PakistaniLegalIdType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legal_id = self.legal_id

        legal_id_type = self.legal_id_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "legalId": legal_id,
                "legalIdType": legal_id_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        legal_id = d.pop("legalId")

        legal_id_type = PakistaniLegalIdType(d.pop("legalIdType"))

        international_wire_pakistan_specific_data = cls(
            legal_id=legal_id,
            legal_id_type=legal_id_type,
        )

        international_wire_pakistan_specific_data.additional_properties = d
        return international_wire_pakistan_specific_data

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
