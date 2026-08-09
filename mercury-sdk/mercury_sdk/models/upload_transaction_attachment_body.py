from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.upload_transaction_attachment_body_attachment_type import UploadTransactionAttachmentBodyAttachmentType
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="UploadTransactionAttachmentBody")


@_attrs_define
class UploadTransactionAttachmentBody:
    """
    Attributes:
        file (File): The file to upload
        attachment_type (UploadTransactionAttachmentBodyAttachmentType | Unset): Type of attachment: 'receipt', 'bill',
            or 'other'. Defaults to 'other'.
    """

    file: File
    attachment_type: UploadTransactionAttachmentBodyAttachmentType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        attachment_type: str | Unset = UNSET
        if not isinstance(self.attachment_type, Unset):
            attachment_type = self.attachment_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if attachment_type is not UNSET:
            field_dict["attachmentType"] = attachment_type

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.attachment_type, Unset):
            files.append(("attachmentType", (None, str(self.attachment_type.value).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        _attachment_type = d.pop("attachmentType", UNSET)
        attachment_type: UploadTransactionAttachmentBodyAttachmentType | Unset
        if isinstance(_attachment_type, Unset):
            attachment_type = UNSET
        else:
            attachment_type = UploadTransactionAttachmentBodyAttachmentType(_attachment_type)

        upload_transaction_attachment_body = cls(
            file=file,
            attachment_type=attachment_type,
        )

        upload_transaction_attachment_body.additional_properties = d
        return upload_transaction_attachment_body

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
