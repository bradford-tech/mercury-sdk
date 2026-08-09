from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.safe_request_investor_type import SafeRequestInvestorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="APISafeRequestInvestor")


@_attrs_define
class APISafeRequestInvestor:
    """Details about the investor buying the equity.

    Attributes:
        investor_type (SafeRequestInvestorType):
        legal_entity_name (str):
        signatory_email (str):
        signatory_name (str):
        additional_bylines (None | str | Unset):
        address (None | str | Unset):
        signatory_title (None | str | Unset):
    """

    investor_type: SafeRequestInvestorType
    legal_entity_name: str
    signatory_email: str
    signatory_name: str
    additional_bylines: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    signatory_title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        investor_type = self.investor_type.value

        legal_entity_name = self.legal_entity_name

        signatory_email = self.signatory_email

        signatory_name = self.signatory_name

        additional_bylines: None | str | Unset
        if isinstance(self.additional_bylines, Unset):
            additional_bylines = UNSET
        else:
            additional_bylines = self.additional_bylines

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        signatory_title: None | str | Unset
        if isinstance(self.signatory_title, Unset):
            signatory_title = UNSET
        else:
            signatory_title = self.signatory_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "investorType": investor_type,
                "legalEntityName": legal_entity_name,
                "signatoryEmail": signatory_email,
                "signatoryName": signatory_name,
            }
        )
        if additional_bylines is not UNSET:
            field_dict["additionalBylines"] = additional_bylines
        if address is not UNSET:
            field_dict["address"] = address
        if signatory_title is not UNSET:
            field_dict["signatoryTitle"] = signatory_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        investor_type = SafeRequestInvestorType(d.pop("investorType"))

        legal_entity_name = d.pop("legalEntityName")

        signatory_email = d.pop("signatoryEmail")

        signatory_name = d.pop("signatoryName")

        def _parse_additional_bylines(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        additional_bylines = _parse_additional_bylines(d.pop("additionalBylines", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_signatory_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signatory_title = _parse_signatory_title(d.pop("signatoryTitle", UNSET))

        api_safe_request_investor = cls(
            investor_type=investor_type,
            legal_entity_name=legal_entity_name,
            signatory_email=signatory_email,
            signatory_name=signatory_name,
            additional_bylines=additional_bylines,
            address=address,
            signatory_title=signatory_title,
        )

        api_safe_request_investor.additional_properties = d
        return api_safe_request_investor

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
