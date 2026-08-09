from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="APISafeRequestOrganization")


@_attrs_define
class APISafeRequestOrganization:
    """Details about the organization selling the equity

    Attributes:
        legal_entity_name (str):
        signatory_email (str):
        signatory_name (str):
        signatory_title (str):
    """

    legal_entity_name: str
    signatory_email: str
    signatory_name: str
    signatory_title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legal_entity_name = self.legal_entity_name

        signatory_email = self.signatory_email

        signatory_name = self.signatory_name

        signatory_title = self.signatory_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "legalEntityName": legal_entity_name,
                "signatoryEmail": signatory_email,
                "signatoryName": signatory_name,
                "signatoryTitle": signatory_title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        legal_entity_name = d.pop("legalEntityName")

        signatory_email = d.pop("signatoryEmail")

        signatory_name = d.pop("signatoryName")

        signatory_title = d.pop("signatoryTitle")

        api_safe_request_organization = cls(
            legal_entity_name=legal_entity_name,
            signatory_email=signatory_email,
            signatory_name=signatory_name,
            signatory_title=signatory_title,
        )

        api_safe_request_organization.additional_properties = d
        return api_safe_request_organization

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
