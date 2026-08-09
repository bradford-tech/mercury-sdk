from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrganizationDBA")


@_attrs_define
class OrganizationDBA:
    """DBA (Doing Business As) information

    Attributes:
        dba_is_default (bool):  Whether this DBA is set as the default for payments
        dba_name (str):  The DBA name
    """

    dba_is_default: bool
    dba_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dba_is_default = self.dba_is_default

        dba_name = self.dba_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dbaIsDefault": dba_is_default,
                "dbaName": dba_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dba_is_default = d.pop("dbaIsDefault")

        dba_name = d.pop("dbaName")

        organization_dba = cls(
            dba_is_default=dba_is_default,
            dba_name=dba_name,
        )

        organization_dba.additional_properties = d
        return organization_dba

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
