from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.swift_bank_account_type import SwiftBankAccountType

T = TypeVar("T", bound="InternationalWireDominicanRepublicSpecificData")


@_attrs_define
class InternationalWireDominicanRepublicSpecificData:
    """
    Attributes:
        account_type (SwiftBankAccountType):
        legal_id (str):
    """

    account_type: SwiftBankAccountType
    legal_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_type = self.account_type.value

        legal_id = self.legal_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountType": account_type,
                "legalId": legal_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_type = SwiftBankAccountType(d.pop("accountType"))

        legal_id = d.pop("legalId")

        international_wire_dominican_republic_specific_data = cls(
            account_type=account_type,
            legal_id=legal_id,
        )

        international_wire_dominican_republic_specific_data.additional_properties = d
        return international_wire_dominican_republic_specific_data

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
