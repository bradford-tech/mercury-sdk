from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.electronic_account_type import ElectronicAccountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_without_name import AddressWithoutName


T = TypeVar("T", bound="ElectronicRoutingInfo")


@_attrs_define
class ElectronicRoutingInfo:
    """
    Attributes:
        account_number (str):
        electronic_account_type (ElectronicAccountType):
        routing_number (str):
        address (AddressWithoutName | None | Unset):
        bank_name (None | str | Unset):
    """

    account_number: str
    electronic_account_type: ElectronicAccountType
    routing_number: str
    address: AddressWithoutName | None | Unset = UNSET
    bank_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.address_without_name import AddressWithoutName

        account_number = self.account_number

        electronic_account_type = self.electronic_account_type.value

        routing_number = self.routing_number

        address: dict[str, Any] | None | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, AddressWithoutName):
            address = self.address.to_dict()
        else:
            address = self.address

        bank_name: None | str | Unset
        if isinstance(self.bank_name, Unset):
            bank_name = UNSET
        else:
            bank_name = self.bank_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountNumber": account_number,
                "electronicAccountType": electronic_account_type,
                "routingNumber": routing_number,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if bank_name is not UNSET:
            field_dict["bankName"] = bank_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_without_name import AddressWithoutName

        d = dict(src_dict)
        account_number = d.pop("accountNumber")

        electronic_account_type = ElectronicAccountType(d.pop("electronicAccountType"))

        routing_number = d.pop("routingNumber")

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

        def _parse_bank_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_name = _parse_bank_name(d.pop("bankName", UNSET))

        electronic_routing_info = cls(
            account_number=account_number,
            electronic_account_type=electronic_account_type,
            routing_number=routing_number,
            address=address,
            bank_name=bank_name,
        )

        electronic_routing_info.additional_properties = d
        return electronic_routing_info

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
