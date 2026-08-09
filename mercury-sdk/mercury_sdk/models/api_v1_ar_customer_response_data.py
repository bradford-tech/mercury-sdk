from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_v1_ar_customer_address import ApiV1ArCustomerAddress


T = TypeVar("T", bound="ApiV1ArCustomerResponseData")


@_attrs_define
class ApiV1ArCustomerResponseData:
    """Response data for Accounts Receivable customer API endpoints

    Attributes:
        email (str):  Email of customer.
        id (UUID):  ArCustomerId
        name (str):  Name of customer.
        address (ApiV1ArCustomerAddress | None | Unset):  Address of customer.
        deleted_at (datetime.datetime | None | Unset):  The time the customer was deleted, if it was deleted. Example:
            2016-07-22T00:00:00Z.
    """

    email: str
    id: UUID
    name: str
    address: ApiV1ArCustomerAddress | None | Unset = UNSET
    deleted_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_ar_customer_address import ApiV1ArCustomerAddress

        email = self.email

        id = str(self.id)

        name = self.name

        address: dict[str, Any] | None | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, ApiV1ArCustomerAddress):
            address = self.address.to_dict()
        else:
            address = self.address

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "id": id,
                "name": name,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_ar_customer_address import ApiV1ArCustomerAddress

        d = dict(src_dict)
        email = d.pop("email")

        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_address(data: object) -> ApiV1ArCustomerAddress | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = ApiV1ArCustomerAddress.from_dict(data)

                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiV1ArCustomerAddress | None | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_deleted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))

        api_v1_ar_customer_response_data = cls(
            email=email,
            id=id,
            name=name,
            address=address,
            deleted_at=deleted_at,
        )

        api_v1_ar_customer_response_data.additional_properties = d
        return api_v1_ar_customer_response_data

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
