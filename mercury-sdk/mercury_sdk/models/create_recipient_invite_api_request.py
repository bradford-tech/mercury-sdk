from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_method import PaymentMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRecipientInviteApiRequest")


@_attrs_define
class CreateRecipientInviteApiRequest:
    """Request body for creating a recipient invite.

    Attributes:
        contact_email (str):  Contact email the invite is sent to. When 'recipientId' is present, updates the
            recipient's contact email to this value.
        payment_methods (list[PaymentMethod]):  Payment methods the recipient may submit details for.
        require_tax_document (bool):  Whether the recipient must upload a tax document.
        send_email (bool):  When true, sends an Email to the invitee. When false, does not send an email to the invitee.
        name (None | str | Unset):  Name the invite is created for. This field is required when 'recipientId' is absent.
             When 'recipientId' is present, this field is optional and updates the recipient's name to this value.
        notes (None | str | Unset):  Optional notes shown to the recipient.
        organization_name_on_request (None | str | Unset):  Optional organization name to display on the request.
        recipient_id (None | Unset | UUID):  The recipient to send the invite to.
    """

    contact_email: str
    payment_methods: list[PaymentMethod]
    require_tax_document: bool
    send_email: bool
    name: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    organization_name_on_request: None | str | Unset = UNSET
    recipient_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact_email = self.contact_email

        payment_methods = []
        for payment_methods_item_data in self.payment_methods:
            payment_methods_item = payment_methods_item_data.value
            payment_methods.append(payment_methods_item)

        require_tax_document = self.require_tax_document

        send_email = self.send_email

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        organization_name_on_request: None | str | Unset
        if isinstance(self.organization_name_on_request, Unset):
            organization_name_on_request = UNSET
        else:
            organization_name_on_request = self.organization_name_on_request

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
                "paymentMethods": payment_methods,
                "requireTaxDocument": require_tax_document,
                "sendEmail": send_email,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if organization_name_on_request is not UNSET:
            field_dict["organizationNameOnRequest"] = organization_name_on_request
        if recipient_id is not UNSET:
            field_dict["recipientId"] = recipient_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contact_email = d.pop("contactEmail")

        payment_methods = []
        _payment_methods = d.pop("paymentMethods")
        for payment_methods_item_data in _payment_methods:
            payment_methods_item = PaymentMethod(payment_methods_item_data)

            payment_methods.append(payment_methods_item)

        require_tax_document = d.pop("requireTaxDocument")

        send_email = d.pop("sendEmail")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_organization_name_on_request(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_name_on_request = _parse_organization_name_on_request(d.pop("organizationNameOnRequest", UNSET))

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

        create_recipient_invite_api_request = cls(
            contact_email=contact_email,
            payment_methods=payment_methods,
            require_tax_document=require_tax_document,
            send_email=send_email,
            name=name,
            notes=notes,
            organization_name_on_request=organization_name_on_request,
            recipient_id=recipient_id,
        )

        create_recipient_invite_api_request.additional_properties = d
        return create_recipient_invite_api_request

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
