from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.address_without_name import AddressWithoutName


T = TypeVar("T", bound="DomesticWireRoutingInfoRaw")


@_attrs_define
class DomesticWireRoutingInfoRaw:
    """
    Attributes:
        account_number (str):  The account number of the bank account to use for domestic wire payments.
        address (AddressWithoutName):
        routing_number (str):  The routing number of the bank account to use for domestic wire payments.
    """

    account_number: str
    address: AddressWithoutName
    routing_number: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_number = self.account_number

        address = self.address.to_dict()

        routing_number = self.routing_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountNumber": account_number,
                "address": address,
                "routingNumber": routing_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_without_name import AddressWithoutName

        d = dict(src_dict)
        account_number = d.pop("accountNumber")

        address = AddressWithoutName.from_dict(d.pop("address"))

        routing_number = d.pop("routingNumber")

        domestic_wire_routing_info_raw = cls(
            account_number=account_number,
            address=address,
            routing_number=routing_number,
        )

        domestic_wire_routing_info_raw.additional_properties = d
        return domestic_wire_routing_info_raw

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
