from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.electronic_account_type import ElectronicAccountType

if TYPE_CHECKING:
    from ..models.address_without_name import AddressWithoutName


T = TypeVar("T", bound="ElectronicRoutingInfoRaw")


@_attrs_define
class ElectronicRoutingInfoRaw:
    """
    Attributes:
        account_number (str):  The account number of the bank account to use for ACH payments.
        address (AddressWithoutName):
        electronic_account_type (ElectronicAccountType):
        routing_number (str):  The routing number of the bank account to use for ACH payments.
    """

    account_number: str
    address: AddressWithoutName
    electronic_account_type: ElectronicAccountType
    routing_number: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_number = self.account_number

        address = self.address.to_dict()

        electronic_account_type = self.electronic_account_type.value

        routing_number = self.routing_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountNumber": account_number,
                "address": address,
                "electronicAccountType": electronic_account_type,
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

        electronic_account_type = ElectronicAccountType(d.pop("electronicAccountType"))

        routing_number = d.pop("routingNumber")

        electronic_routing_info_raw = cls(
            account_number=account_number,
            address=address,
            electronic_account_type=electronic_account_type,
            routing_number=routing_number,
        )

        electronic_routing_info_raw.additional_properties = d
        return electronic_routing_info_raw

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
