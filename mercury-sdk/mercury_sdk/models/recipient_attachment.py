from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tax_form_type import TaxFormType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RecipientAttachment")


@_attrs_define
class RecipientAttachment:
    """
    Attributes:
        file_name (str):  Name of the uploaded file
        uploaded_at (datetime.datetime):  Timestamp when the attachment was uploaded Example: 2016-07-22T00:00:00Z.
        url (str):  Presigned URL to download the attachment (valid for 12 hours)
        form_type (None | TaxFormType | Unset):  The tax form type (W-9 for US persons, W-8BEN for foreign individuals,
            W-8BEN-E for foreign entities)
    """

    file_name: str
    uploaded_at: datetime.datetime
    url: str
    form_type: None | TaxFormType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

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

        recipient_attachment = cls(
            file_name=file_name,
            uploaded_at=uploaded_at,
            url=url,
            form_type=form_type,
        )

        recipient_attachment.additional_properties = d
        return recipient_attachment

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
