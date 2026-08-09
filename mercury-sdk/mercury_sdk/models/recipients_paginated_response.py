from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.recipient_info import RecipientInfo
    from ..models.recipients_paginated_response_page import RecipientsPaginatedResponsePage


T = TypeVar("T", bound="RecipientsPaginatedResponse")


@_attrs_define
class RecipientsPaginatedResponse:
    """
    Attributes:
        page (RecipientsPaginatedResponsePage):  Pagination information including cursors for navigating to
            next/previous pages
        recipients (list[RecipientInfo]):  List of recipients in the current page
        total (int):  Total number of recipients in the current page
    """

    page: RecipientsPaginatedResponsePage
    recipients: list[RecipientInfo]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page.to_dict()

        recipients = []
        for recipients_item_data in self.recipients:
            recipients_item = recipients_item_data.to_dict()
            recipients.append(recipients_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "recipients": recipients,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipient_info import RecipientInfo
        from ..models.recipients_paginated_response_page import RecipientsPaginatedResponsePage

        d = dict(src_dict)
        page = RecipientsPaginatedResponsePage.from_dict(d.pop("page"))

        recipients = []
        _recipients = d.pop("recipients")
        for recipients_item_data in _recipients:
            recipients_item = RecipientInfo.from_dict(recipients_item_data)

            recipients.append(recipients_item)

        total = d.pop("total")

        recipients_paginated_response = cls(
            page=page,
            recipients=recipients,
            total=total,
        )

        recipients_paginated_response.additional_properties = d
        return recipients_paginated_response

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
