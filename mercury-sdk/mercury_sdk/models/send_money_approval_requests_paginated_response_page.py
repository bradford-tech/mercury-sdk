from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendMoneyApprovalRequestsPaginatedResponsePage")


@_attrs_define
class SendMoneyApprovalRequestsPaginatedResponsePage:
    """
    Attributes:
        next_page (UUID | Unset): ID for the send money approval request
        previous_page (UUID | Unset): ID for the send money approval request
    """

    next_page: UUID | Unset = UNSET
    previous_page: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_page: str | Unset = UNSET
        if not isinstance(self.next_page, Unset):
            next_page = str(self.next_page)

        previous_page: str | Unset = UNSET
        if not isinstance(self.previous_page, Unset):
            previous_page = str(self.previous_page)

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
        _next_page = d.pop("nextPage", UNSET)
        next_page: UUID | Unset
        if isinstance(_next_page, Unset):
            next_page = UNSET
        else:
            next_page = UUID(_next_page)

        _previous_page = d.pop("previousPage", UNSET)
        previous_page: UUID | Unset
        if isinstance(_previous_page, Unset):
            previous_page = UNSET
        else:
            previous_page = UUID(_previous_page)

        send_money_approval_requests_paginated_response_page = cls(
            next_page=next_page,
            previous_page=previous_page,
        )

        send_money_approval_requests_paginated_response_page.additional_properties = d
        return send_money_approval_requests_paginated_response_page

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
