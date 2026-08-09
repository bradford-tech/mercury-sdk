from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transaction_attachment_type import TransactionAttachmentType

T = TypeVar("T", bound="TransactionAttachment")


@_attrs_define
class TransactionAttachment:
    """
    Attributes:
        attachment_type (TransactionAttachmentType):
        file_name (str):
        url (str):
    """

    attachment_type: TransactionAttachmentType
    file_name: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachment_type = self.attachment_type.value

        file_name = self.file_name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attachmentType": attachment_type,
                "fileName": file_name,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attachment_type = TransactionAttachmentType(d.pop("attachmentType"))

        file_name = d.pop("fileName")

        url = d.pop("url")

        transaction_attachment = cls(
            attachment_type=attachment_type,
            file_name=file_name,
            url=url,
        )

        transaction_attachment.additional_properties = d
        return transaction_attachment

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
