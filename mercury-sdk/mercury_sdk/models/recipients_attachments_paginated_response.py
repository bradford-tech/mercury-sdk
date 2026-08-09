from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.recipient_attachment_with_id import RecipientAttachmentWithId
    from ..models.recipients_attachments_paginated_response_page import RecipientsAttachmentsPaginatedResponsePage


T = TypeVar("T", bound="RecipientsAttachmentsPaginatedResponse")


@_attrs_define
class RecipientsAttachmentsPaginatedResponse:
    """
    Attributes:
        attachments (list[RecipientAttachmentWithId]):  List of attachments with recipient IDs
        page (RecipientsAttachmentsPaginatedResponsePage):  Pagination information
        total (int):  Total number of attachments in the current page
    """

    attachments: list[RecipientAttachmentWithId]
    page: RecipientsAttachmentsPaginatedResponsePage
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()
            attachments.append(attachments_item)

        page = self.page.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attachments": attachments,
                "page": page,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recipient_attachment_with_id import RecipientAttachmentWithId
        from ..models.recipients_attachments_paginated_response_page import RecipientsAttachmentsPaginatedResponsePage

        d = dict(src_dict)
        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = RecipientAttachmentWithId.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        page = RecipientsAttachmentsPaginatedResponsePage.from_dict(d.pop("page"))

        total = d.pop("total")

        recipients_attachments_paginated_response = cls(
            attachments=attachments,
            page=page,
            total=total,
        )

        recipients_attachments_paginated_response.additional_properties = d
        return recipients_attachments_paginated_response

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
