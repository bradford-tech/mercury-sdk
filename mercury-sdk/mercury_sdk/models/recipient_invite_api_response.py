from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_method import PaymentMethod
from ..models.recipient_invite_status import RecipientInviteStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RecipientInviteApiResponse")


@_attrs_define
class RecipientInviteApiResponse:
    """
    Attributes:
        contact_email (str):  Recipient contact email the invite was created for.
        created_at (datetime.datetime):  When the invite was created. Example: 2016-07-22T00:00:00Z.
        id (str):  The invite's id, also embedded in 'onboardingUrl'.
        name (str):  Recipient name the invite was created for.
        onboarding_url (str):  URL where the recipient submits their payment details.
        payment_methods (list[PaymentMethod]):  Payment methods the recipient may submit details for.
        require_tax_document (bool):  Whether the recipient must upload a tax document.
        status (RecipientInviteStatus):
        expires_at (datetime.datetime | None | Unset):  When the invite expires, if it has an expiry. Example:
            2016-07-22T00:00:00Z.
        notes (None | str | Unset):  Notes shown to the recipient, if any.
        recipient_id (None | Unset | UUID):  The existing recipient this invite is for, if any.
    """

    contact_email: str
    created_at: datetime.datetime
    id: str
    name: str
    onboarding_url: str
    payment_methods: list[PaymentMethod]
    require_tax_document: bool
    status: RecipientInviteStatus
    expires_at: datetime.datetime | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    recipient_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact_email = self.contact_email

        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        onboarding_url = self.onboarding_url

        payment_methods = []
        for payment_methods_item_data in self.payment_methods:
            payment_methods_item = payment_methods_item_data.value
            payment_methods.append(payment_methods_item)

        require_tax_document = self.require_tax_document

        status = self.status.value

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        recipient_id: None | str | Unset
        if isinstance(self.recipient_id, Unset):
            recipient_id = UNSET
        elif isinstance(self.recipient_id, UUID):
            recipient_id = str(self.recipient_id)
        else:
            recipient_id = self.recipient_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contactEmail": contact_email,
                "createdAt": created_at,
                "id": id,
                "name": name,
                "onboardingUrl": onboarding_url,
                "paymentMethods": payment_methods,
                "requireTaxDocument": require_tax_document,
                "status": status,
            }
        )
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if notes is not UNSET:
            field_dict["notes"] = notes
        if recipient_id is not UNSET:
            field_dict["recipientId"] = recipient_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contact_email = d.pop("contactEmail")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        id = d.pop("id")

        name = d.pop("name")

        onboarding_url = d.pop("onboardingUrl")

        payment_methods = []
        _payment_methods = d.pop("paymentMethods")
        for payment_methods_item_data in _payment_methods:
            payment_methods_item = PaymentMethod(payment_methods_item_data)

            payment_methods.append(payment_methods_item)

        require_tax_document = d.pop("requireTaxDocument")

        status = RecipientInviteStatus(d.pop("status"))

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_recipient_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recipient_id_type_0 = UUID(data)

                return recipient_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        recipient_id = _parse_recipient_id(d.pop("recipientId", UNSET))

        recipient_invite_api_response = cls(
            contact_email=contact_email,
            created_at=created_at,
            id=id,
            name=name,
            onboarding_url=onboarding_url,
            payment_methods=payment_methods,
            require_tax_document=require_tax_document,
            status=status,
            expires_at=expires_at,
            notes=notes,
            recipient_id=recipient_id,
        )

        recipient_invite_api_response.additional_properties = d
        return recipient_invite_api_response

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
