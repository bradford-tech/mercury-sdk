from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_data import AddressData
    from ..models.check_info_raw import CheckInfoRaw
    from ..models.domestic_wire_routing_info_raw import DomesticWireRoutingInfoRaw
    from ..models.electronic_routing_info_raw import ElectronicRoutingInfoRaw


T = TypeVar("T", bound="EditRecipientRequest")


@_attrs_define
class EditRecipientRequest:
    """
    Attributes:
        address (AddressData | Unset):
        check_info (CheckInfoRaw | Unset):
        contact_email (str | Unset): Contact email address of the recipient
        domestic_wire_routing_info (DomesticWireRoutingInfoRaw | Unset):
        electronic_routing_info (ElectronicRoutingInfoRaw | Unset):
        emails (list[str] | Unset):
        name (str | Unset):
        nickname (str | Unset):
    """

    address: AddressData | Unset = UNSET
    check_info: CheckInfoRaw | Unset = UNSET
    contact_email: str | Unset = UNSET
    domestic_wire_routing_info: DomesticWireRoutingInfoRaw | Unset = UNSET
    electronic_routing_info: ElectronicRoutingInfoRaw | Unset = UNSET
    emails: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    nickname: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        check_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_info, Unset):
            check_info = self.check_info.to_dict()

        contact_email = self.contact_email

        domestic_wire_routing_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domestic_wire_routing_info, Unset):
            domestic_wire_routing_info = self.domestic_wire_routing_info.to_dict()

        electronic_routing_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.electronic_routing_info, Unset):
            electronic_routing_info = self.electronic_routing_info.to_dict()

        emails: list[str] | Unset = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        name = self.name

        nickname = self.nickname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if check_info is not UNSET:
            field_dict["checkInfo"] = check_info
        if contact_email is not UNSET:
            field_dict["contactEmail"] = contact_email
        if domestic_wire_routing_info is not UNSET:
            field_dict["domesticWireRoutingInfo"] = domestic_wire_routing_info
        if electronic_routing_info is not UNSET:
            field_dict["electronicRoutingInfo"] = electronic_routing_info
        if emails is not UNSET:
            field_dict["emails"] = emails
        if name is not UNSET:
            field_dict["name"] = name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_data import AddressData
        from ..models.check_info_raw import CheckInfoRaw
        from ..models.domestic_wire_routing_info_raw import DomesticWireRoutingInfoRaw
        from ..models.electronic_routing_info_raw import ElectronicRoutingInfoRaw

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: AddressData | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = AddressData.from_dict(_address)

        _check_info = d.pop("checkInfo", UNSET)
        check_info: CheckInfoRaw | Unset
        if isinstance(_check_info, Unset):
            check_info = UNSET
        else:
            check_info = CheckInfoRaw.from_dict(_check_info)

        contact_email = d.pop("contactEmail", UNSET)

        _domestic_wire_routing_info = d.pop("domesticWireRoutingInfo", UNSET)
        domestic_wire_routing_info: DomesticWireRoutingInfoRaw | Unset
        if isinstance(_domestic_wire_routing_info, Unset):
            domestic_wire_routing_info = UNSET
        else:
            domestic_wire_routing_info = DomesticWireRoutingInfoRaw.from_dict(_domestic_wire_routing_info)

        _electronic_routing_info = d.pop("electronicRoutingInfo", UNSET)
        electronic_routing_info: ElectronicRoutingInfoRaw | Unset
        if isinstance(_electronic_routing_info, Unset):
            electronic_routing_info = UNSET
        else:
            electronic_routing_info = ElectronicRoutingInfoRaw.from_dict(_electronic_routing_info)

        emails = cast(list[str], d.pop("emails", UNSET))

        name = d.pop("name", UNSET)

        nickname = d.pop("nickname", UNSET)

        edit_recipient_request = cls(
            address=address,
            check_info=check_info,
            contact_email=contact_email,
            domestic_wire_routing_info=domestic_wire_routing_info,
            electronic_routing_info=electronic_routing_info,
            emails=emails,
            name=name,
            nickname=nickname,
        )

        edit_recipient_request.additional_properties = d
        return edit_recipient_request

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
