from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_v1_ar_customer_address_input import ApiV1ArCustomerAddressInput


T = TypeVar("T", bound="ApiV1ArCustomerCreateRequest")


@_attrs_define
class ApiV1ArCustomerCreateRequest:
    """Request data to create a customer using the public api

    Attributes:
        email (str):  The email address for the customer.
        name (str):  The name of the customer.
        address (ApiV1ArCustomerAddressInput | None | Unset):  The address for the customer.
    """

    email: str
    name: str
    address: ApiV1ArCustomerAddressInput | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_ar_customer_address_input import ApiV1ArCustomerAddressInput

        email = self.email

        name = self.name

        address: dict[str, Any] | None | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, ApiV1ArCustomerAddressInput):
            address = self.address.to_dict()
        else:
            address = self.address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "name": name,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_ar_customer_address_input import ApiV1ArCustomerAddressInput

        d = dict(src_dict)
        email = d.pop("email")

        name = d.pop("name")

        def _parse_address(data: object) -> ApiV1ArCustomerAddressInput | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = ApiV1ArCustomerAddressInput.from_dict(data)

                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiV1ArCustomerAddressInput | None | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        api_v1_ar_customer_create_request = cls(
            email=email,
            name=name,
            address=address,
        )

        api_v1_ar_customer_create_request.additional_properties = d
        return api_v1_ar_customer_create_request

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
