from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.simple_purpose_category import SimplePurposeCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="SimplePurpose")


@_attrs_define
class SimplePurpose:
    """
    Attributes:
        category (SimplePurposeCategory): Payment category.
        additional_info (str | Unset): Additional information. Required for: Vendor (vendor name), Contractor
            (contractor name), Other (payment description). Optional for Subsidiary (subsidiary name). Not accepted for any
            other categories.
    """

    category: SimplePurposeCategory
    additional_info: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        additional_info = self.additional_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
            }
        )
        if additional_info is not UNSET:
            field_dict["additionalInfo"] = additional_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = SimplePurposeCategory(d.pop("category"))

        additional_info = d.pop("additionalInfo", UNSET)

        simple_purpose = cls(
            category=category,
            additional_info=additional_info,
        )

        simple_purpose.additional_properties = d
        return simple_purpose

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
