from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_v1_ar_attachment_response_data import ApiV1ArAttachmentResponseData


T = TypeVar("T", bound="ApiV1ArAttachmentsResponseData")


@_attrs_define
class ApiV1ArAttachmentsResponseData:
    """The response type for fetching attachments related to an AR Invoice.

    Attributes:
        attachments (list[ApiV1ArAttachmentResponseData]):  The list of attachments
    """

    attachments: list[ApiV1ArAttachmentResponseData]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()
            attachments.append(attachments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attachments": attachments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_ar_attachment_response_data import ApiV1ArAttachmentResponseData

        d = dict(src_dict)
        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = ApiV1ArAttachmentResponseData.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        api_v1_ar_attachments_response_data = cls(
            attachments=attachments,
        )

        api_v1_ar_attachments_response_data.additional_properties = d
        return api_v1_ar_attachments_response_data

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
