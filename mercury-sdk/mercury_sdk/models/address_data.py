from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.us_state import USState
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddressData")


@_attrs_define
class AddressData:
    """
    Attributes:
        address1 (str):
        city (str):
        postal_code (str):
        address2 (None | str | Unset):
        state (None | Unset | USState):
    """

    address1: str
    city: str
    postal_code: str
    address2: None | str | Unset = UNSET
    state: None | Unset | USState = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address1 = self.address1

        city = self.city

        postal_code = self.postal_code

        address2: None | str | Unset
        if isinstance(self.address2, Unset):
            address2 = UNSET
        else:
            address2 = self.address2

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, USState):
            state = self.state.value
        else:
            state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address1": address1,
                "city": city,
                "postalCode": postal_code,
            }
        )
        if address2 is not UNSET:
            field_dict["address2"] = address2
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address1 = d.pop("address1")

        city = d.pop("city")

        postal_code = d.pop("postalCode")

        def _parse_address2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address2 = _parse_address2(d.pop("address2", UNSET))

        def _parse_state(data: object) -> None | Unset | USState:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_0 = USState(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | USState, data)

        state = _parse_state(d.pop("state", UNSET))

        address_data = cls(
            address1=address1,
            city=city,
            postal_code=postal_code,
            address2=address2,
            state=state,
        )

        address_data.additional_properties = d
        return address_data

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
