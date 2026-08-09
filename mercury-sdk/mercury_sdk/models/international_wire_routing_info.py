from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_without_name import AddressWithoutName
    from ..models.international_wire_correspondent_info import InternationalWireCorrespondentInfo
    from ..models.international_wire_country_specific_data import InternationalWireCountrySpecificData
    from ..models.swift_code_data import SwiftCodeData


T = TypeVar("T", bound="InternationalWireRoutingInfo")


@_attrs_define
class InternationalWireRoutingInfo:
    """
    Attributes:
        country_specific (InternationalWireCountrySpecificData):
        iban (str):
        swift_code (str):
        address (AddressWithoutName | None | Unset):
        bank_details (None | SwiftCodeData | Unset):
        correspondent_info (InternationalWireCorrespondentInfo | None | Unset):
        email_address (None | str | Unset):
        phone_number (None | str | Unset):
    """

    country_specific: InternationalWireCountrySpecificData
    iban: str
    swift_code: str
    address: AddressWithoutName | None | Unset = UNSET
    bank_details: None | SwiftCodeData | Unset = UNSET
    correspondent_info: InternationalWireCorrespondentInfo | None | Unset = UNSET
    email_address: None | str | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.address_without_name import AddressWithoutName
        from ..models.international_wire_correspondent_info import InternationalWireCorrespondentInfo
        from ..models.swift_code_data import SwiftCodeData

        country_specific = self.country_specific.to_dict()

        iban = self.iban

        swift_code = self.swift_code

        address: dict[str, Any] | None | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, AddressWithoutName):
            address = self.address.to_dict()
        else:
            address = self.address

        bank_details: dict[str, Any] | None | Unset
        if isinstance(self.bank_details, Unset):
            bank_details = UNSET
        elif isinstance(self.bank_details, SwiftCodeData):
            bank_details = self.bank_details.to_dict()
        else:
            bank_details = self.bank_details

        correspondent_info: dict[str, Any] | None | Unset
        if isinstance(self.correspondent_info, Unset):
            correspondent_info = UNSET
        elif isinstance(self.correspondent_info, InternationalWireCorrespondentInfo):
            correspondent_info = self.correspondent_info.to_dict()
        else:
            correspondent_info = self.correspondent_info

        email_address: None | str | Unset
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        else:
            email_address = self.email_address

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "countrySpecific": country_specific,
                "iban": iban,
                "swiftCode": swift_code,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if bank_details is not UNSET:
            field_dict["bankDetails"] = bank_details
        if correspondent_info is not UNSET:
            field_dict["correspondentInfo"] = correspondent_info
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_without_name import AddressWithoutName
        from ..models.international_wire_correspondent_info import InternationalWireCorrespondentInfo
        from ..models.international_wire_country_specific_data import InternationalWireCountrySpecificData
        from ..models.swift_code_data import SwiftCodeData

        d = dict(src_dict)
        country_specific = InternationalWireCountrySpecificData.from_dict(d.pop("countrySpecific"))

        iban = d.pop("iban")

        swift_code = d.pop("swiftCode")

        def _parse_address(data: object) -> AddressWithoutName | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = AddressWithoutName.from_dict(data)

                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AddressWithoutName | None | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_bank_details(data: object) -> None | SwiftCodeData | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bank_details_type_0 = SwiftCodeData.from_dict(data)

                return bank_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SwiftCodeData | Unset, data)

        bank_details = _parse_bank_details(d.pop("bankDetails", UNSET))

        def _parse_correspondent_info(data: object) -> InternationalWireCorrespondentInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                correspondent_info_type_0 = InternationalWireCorrespondentInfo.from_dict(data)

                return correspondent_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireCorrespondentInfo | None | Unset, data)

        correspondent_info = _parse_correspondent_info(d.pop("correspondentInfo", UNSET))

        def _parse_email_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address = _parse_email_address(d.pop("emailAddress", UNSET))

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

        international_wire_routing_info = cls(
            country_specific=country_specific,
            iban=iban,
            swift_code=swift_code,
            address=address,
            bank_details=bank_details,
            correspondent_info=correspondent_info,
            email_address=email_address,
            phone_number=phone_number,
        )

        international_wire_routing_info.additional_properties = d
        return international_wire_routing_info

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
