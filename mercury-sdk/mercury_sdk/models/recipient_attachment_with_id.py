from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tax_form_type import TaxFormType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RecipientAttachmentWithId")


@_attrs_define
class RecipientAttachmentWithId:
    """
    Attributes:
        file_name (str):  Name of the uploaded file
        id (UUID):  The unique identifier for this attachment
        recipient_id (UUID):  The external ID of the recipient this attachment belongs to
        uploaded_at (datetime.datetime):  Timestamp when the attachment was uploaded Example: 2016-07-22T00:00:00Z.
        url (str):  Presigned URL to download the attachment (valid for 12 hours)
        form_type (None | TaxFormType | Unset):  The tax form type (W-9, W-8BEN, W-8BEN-E, or Unknown)
    """

    file_name: str
    id: UUID
    recipient_id: UUID
    uploaded_at: datetime.datetime
    url: str
    form_type: None | TaxFormType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        id = str(self.id)

        recipient_id = str(self.recipient_id)

        uploaded_at = self.uploaded_at.isoformat()

        url = self.url

        form_type: None | str | Unset
        if isinstance(self.form_type, Unset):
            form_type = UNSET
        elif isinstance(self.form_type, TaxFormType):
            form_type = self.form_type.value
        else:
            form_type = self.form_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileName": file_name,
                "id": id,
                "recipientId": recipient_id,
                "uploadedAt": uploaded_at,
                "url": url,
            }
        )
        if form_type is not UNSET:
            field_dict["formType"] = form_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("fileName")

        id = UUID(d.pop("id"))

        recipient_id = UUID(d.pop("recipientId"))

        uploaded_at = datetime.datetime.fromisoformat(d.pop("uploadedAt"))

        url = d.pop("url")

        def _parse_form_type(data: object) -> None | TaxFormType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                form_type_type_0 = TaxFormType(data)

                return form_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaxFormType | Unset, data)

        form_type = _parse_form_type(d.pop("formType", UNSET))

        recipient_attachment_with_id = cls(
            file_name=file_name,
            id=id,
            recipient_id=recipient_id,
            uploaded_at=uploaded_at,
            url=url,
            form_type=form_type,
        )

        recipient_attachment_with_id.additional_properties = d
        return recipient_attachment_with_id

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
