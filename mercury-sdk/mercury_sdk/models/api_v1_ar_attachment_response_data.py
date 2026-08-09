from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiV1ArAttachmentResponseData")


@_attrs_define
class ApiV1ArAttachmentResponseData:
    """The object representing a file attachment for an invoice.
    The file is not a part of this object itself but information
    for where to download it will be in this object.

       Attributes:
           file_name (str):  The filename for the file.
           id (UUID):  The ID of the attachment object.
           url (str):  The signed download URL for the file itself.
    """

    file_name: str
    id: UUID
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        id = str(self.id)

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileName": file_name,
                "id": id,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("fileName")

        id = UUID(d.pop("id"))

        url = d.pop("url")

        api_v1_ar_attachment_response_data = cls(
            file_name=file_name,
            id=id,
            url=url,
        )

        api_v1_ar_attachment_response_data.additional_properties = d
        return api_v1_ar_attachment_response_data

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
