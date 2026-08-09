from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecipientInviteApiPaginatedResponsePage")


@_attrs_define
class RecipientInviteApiPaginatedResponsePage:
    """Pagination cursors (inviteId) for navigating to next/previous pages.

    Attributes:
        next_page (str | Unset): ID for the invite
        previous_page (str | Unset): ID for the invite
    """

    next_page: str | Unset = UNSET
    previous_page: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_page = self.next_page

        previous_page = self.previous_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_page is not UNSET:
            field_dict["nextPage"] = next_page
        if previous_page is not UNSET:
            field_dict["previousPage"] = previous_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        next_page = d.pop("nextPage", UNSET)

        previous_page = d.pop("previousPage", UNSET)

        recipient_invite_api_paginated_response_page = cls(
            next_page=next_page,
            previous_page=previous_page,
        )

        recipient_invite_api_paginated_response_page.additional_properties = d
        return recipient_invite_api_paginated_response_page

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
