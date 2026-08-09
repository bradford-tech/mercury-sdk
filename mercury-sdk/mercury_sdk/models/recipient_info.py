from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_method import PaymentMethod
from ..models.recipient_status import RecipientStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.address_without_name import AddressWithoutName
    from ..models.check_info import CheckInfo
    from ..models.domestic_wire_routing_info import DomesticWireRoutingInfo
    from ..models.electronic_routing_info import ElectronicRoutingInfo
    from ..models.international_wire_routing_info import InternationalWireRoutingInfo
    from ..models.real_time_payment_routing_info import RealTimePaymentRoutingInfo
    from ..models.recipient_attachment import RecipientAttachment


T = TypeVar("T", bound="RecipientInfo")


@_attrs_define
class RecipientInfo:
    """
    Attributes:
        attachments (list[RecipientAttachment]):
        default_payment_method (PaymentMethod):
        emails (list[str]):
        id (UUID): ID for a Mercury account.
        name (str):
        status (RecipientStatus):
        address (Address | None | Unset):
        check_info (CheckInfo | None | Unset):
        contact_email (None | str | Unset):
        date_last_paid (datetime.datetime | None | Unset):  Example: 2016-07-22T00:00:00Z.
        default_address (AddressWithoutName | None | Unset):
        domestic_wire_routing_info (DomesticWireRoutingInfo | None | Unset):
        electronic_routing_info (ElectronicRoutingInfo | None | Unset):
        international_wire_routing_info (InternationalWireRoutingInfo | None | Unset):
        invite_id (None | str | Unset):
        is_business (bool | None | Unset):
        nickname (None | str | Unset):
        real_time_payment_routing_info (None | RealTimePaymentRoutingInfo | Unset):
    """

    attachments: list[RecipientAttachment]
    default_payment_method: PaymentMethod
    emails: list[str]
    id: UUID
    name: str
    status: RecipientStatus
    address: Address | None | Unset = UNSET
    check_info: CheckInfo | None | Unset = UNSET
    contact_email: None | str | Unset = UNSET
    date_last_paid: datetime.datetime | None | Unset = UNSET
    default_address: AddressWithoutName | None | Unset = UNSET
    domestic_wire_routing_info: DomesticWireRoutingInfo | None | Unset = UNSET
    electronic_routing_info: ElectronicRoutingInfo | None | Unset = UNSET
    international_wire_routing_info: InternationalWireRoutingInfo | None | Unset = UNSET
    invite_id: None | str | Unset = UNSET
    is_business: bool | None | Unset = UNSET
    nickname: None | str | Unset = UNSET
    real_time_payment_routing_info: None | RealTimePaymentRoutingInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.address import Address
        from ..models.address_without_name import AddressWithoutName
        from ..models.check_info import CheckInfo
        from ..models.domestic_wire_routing_info import DomesticWireRoutingInfo
        from ..models.electronic_routing_info import ElectronicRoutingInfo
        from ..models.international_wire_routing_info import InternationalWireRoutingInfo
        from ..models.real_time_payment_routing_info import RealTimePaymentRoutingInfo

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()
            attachments.append(attachments_item)

        default_payment_method = self.default_payment_method.value

        emails = self.emails

        id = str(self.id)

        name = self.name

        status = self.status.value

        address: dict[str, Any] | None | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, Address):
            address = self.address.to_dict()
        else:
            address = self.address

        check_info: dict[str, Any] | None | Unset
        if isinstance(self.check_info, Unset):
            check_info = UNSET
        elif isinstance(self.check_info, CheckInfo):
            check_info = self.check_info.to_dict()
        else:
            check_info = self.check_info

        contact_email: None | str | Unset
        if isinstance(self.contact_email, Unset):
            contact_email = UNSET
        else:
            contact_email = self.contact_email

        date_last_paid: None | str | Unset
        if isinstance(self.date_last_paid, Unset):
            date_last_paid = UNSET
        elif isinstance(self.date_last_paid, datetime.datetime):
            date_last_paid = self.date_last_paid.isoformat()
        else:
            date_last_paid = self.date_last_paid

        default_address: dict[str, Any] | None | Unset
        if isinstance(self.default_address, Unset):
            default_address = UNSET
        elif isinstance(self.default_address, AddressWithoutName):
            default_address = self.default_address.to_dict()
        else:
            default_address = self.default_address

        domestic_wire_routing_info: dict[str, Any] | None | Unset
        if isinstance(self.domestic_wire_routing_info, Unset):
            domestic_wire_routing_info = UNSET
        elif isinstance(self.domestic_wire_routing_info, DomesticWireRoutingInfo):
            domestic_wire_routing_info = self.domestic_wire_routing_info.to_dict()
        else:
            domestic_wire_routing_info = self.domestic_wire_routing_info

        electronic_routing_info: dict[str, Any] | None | Unset
        if isinstance(self.electronic_routing_info, Unset):
            electronic_routing_info = UNSET
        elif isinstance(self.electronic_routing_info, ElectronicRoutingInfo):
            electronic_routing_info = self.electronic_routing_info.to_dict()
        else:
            electronic_routing_info = self.electronic_routing_info

        international_wire_routing_info: dict[str, Any] | None | Unset
        if isinstance(self.international_wire_routing_info, Unset):
            international_wire_routing_info = UNSET
        elif isinstance(self.international_wire_routing_info, InternationalWireRoutingInfo):
            international_wire_routing_info = self.international_wire_routing_info.to_dict()
        else:
            international_wire_routing_info = self.international_wire_routing_info

        invite_id: None | str | Unset
        if isinstance(self.invite_id, Unset):
            invite_id = UNSET
        else:
            invite_id = self.invite_id

        is_business: bool | None | Unset
        if isinstance(self.is_business, Unset):
            is_business = UNSET
        else:
            is_business = self.is_business

        nickname: None | str | Unset
        if isinstance(self.nickname, Unset):
            nickname = UNSET
        else:
            nickname = self.nickname

        real_time_payment_routing_info: dict[str, Any] | None | Unset
        if isinstance(self.real_time_payment_routing_info, Unset):
            real_time_payment_routing_info = UNSET
        elif isinstance(self.real_time_payment_routing_info, RealTimePaymentRoutingInfo):
            real_time_payment_routing_info = self.real_time_payment_routing_info.to_dict()
        else:
            real_time_payment_routing_info = self.real_time_payment_routing_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attachments": attachments,
                "defaultPaymentMethod": default_payment_method,
                "emails": emails,
                "id": id,
                "name": name,
                "status": status,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if check_info is not UNSET:
            field_dict["checkInfo"] = check_info
        if contact_email is not UNSET:
            field_dict["contactEmail"] = contact_email
        if date_last_paid is not UNSET:
            field_dict["dateLastPaid"] = date_last_paid
        if default_address is not UNSET:
            field_dict["defaultAddress"] = default_address
        if domestic_wire_routing_info is not UNSET:
            field_dict["domesticWireRoutingInfo"] = domestic_wire_routing_info
        if electronic_routing_info is not UNSET:
            field_dict["electronicRoutingInfo"] = electronic_routing_info
        if international_wire_routing_info is not UNSET:
            field_dict["internationalWireRoutingInfo"] = international_wire_routing_info
        if invite_id is not UNSET:
            field_dict["inviteId"] = invite_id
        if is_business is not UNSET:
            field_dict["isBusiness"] = is_business
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if real_time_payment_routing_info is not UNSET:
            field_dict["realTimePaymentRoutingInfo"] = real_time_payment_routing_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.address_without_name import AddressWithoutName
        from ..models.check_info import CheckInfo
        from ..models.domestic_wire_routing_info import DomesticWireRoutingInfo
        from ..models.electronic_routing_info import ElectronicRoutingInfo
        from ..models.international_wire_routing_info import InternationalWireRoutingInfo
        from ..models.real_time_payment_routing_info import RealTimePaymentRoutingInfo
        from ..models.recipient_attachment import RecipientAttachment

        d = dict(src_dict)
        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = RecipientAttachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        default_payment_method = PaymentMethod(d.pop("defaultPaymentMethod"))

        emails = cast(list[str], d.pop("emails"))

        id = UUID(d.pop("id"))

        name = d.pop("name")

        status = RecipientStatus(d.pop("status"))

        def _parse_address(data: object) -> Address | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = Address.from_dict(data)

                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Address | None | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_check_info(data: object) -> CheckInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                check_info_type_0 = CheckInfo.from_dict(data)

                return check_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CheckInfo | None | Unset, data)

        check_info = _parse_check_info(d.pop("checkInfo", UNSET))

        def _parse_contact_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_email = _parse_contact_email(d.pop("contactEmail", UNSET))

        def _parse_date_last_paid(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_last_paid_type_0 = datetime.datetime.fromisoformat(data)

                return date_last_paid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_last_paid = _parse_date_last_paid(d.pop("dateLastPaid", UNSET))

        def _parse_default_address(data: object) -> AddressWithoutName | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_address_type_0 = AddressWithoutName.from_dict(data)

                return default_address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AddressWithoutName | None | Unset, data)

        default_address = _parse_default_address(d.pop("defaultAddress", UNSET))

        def _parse_domestic_wire_routing_info(data: object) -> DomesticWireRoutingInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                domestic_wire_routing_info_type_0 = DomesticWireRoutingInfo.from_dict(data)

                return domestic_wire_routing_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DomesticWireRoutingInfo | None | Unset, data)

        domestic_wire_routing_info = _parse_domestic_wire_routing_info(d.pop("domesticWireRoutingInfo", UNSET))

        def _parse_electronic_routing_info(data: object) -> ElectronicRoutingInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                electronic_routing_info_type_0 = ElectronicRoutingInfo.from_dict(data)

                return electronic_routing_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ElectronicRoutingInfo | None | Unset, data)

        electronic_routing_info = _parse_electronic_routing_info(d.pop("electronicRoutingInfo", UNSET))

        def _parse_international_wire_routing_info(data: object) -> InternationalWireRoutingInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                international_wire_routing_info_type_0 = InternationalWireRoutingInfo.from_dict(data)

                return international_wire_routing_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternationalWireRoutingInfo | None | Unset, data)

        international_wire_routing_info = _parse_international_wire_routing_info(
            d.pop("internationalWireRoutingInfo", UNSET)
        )

        def _parse_invite_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invite_id = _parse_invite_id(d.pop("inviteId", UNSET))

        def _parse_is_business(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_business = _parse_is_business(d.pop("isBusiness", UNSET))

        def _parse_nickname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nickname = _parse_nickname(d.pop("nickname", UNSET))

        def _parse_real_time_payment_routing_info(data: object) -> None | RealTimePaymentRoutingInfo | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                real_time_payment_routing_info_type_0 = RealTimePaymentRoutingInfo.from_dict(data)

                return real_time_payment_routing_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RealTimePaymentRoutingInfo | Unset, data)

        real_time_payment_routing_info = _parse_real_time_payment_routing_info(
            d.pop("realTimePaymentRoutingInfo", UNSET)
        )

        recipient_info = cls(
            attachments=attachments,
            default_payment_method=default_payment_method,
            emails=emails,
            id=id,
            name=name,
            status=status,
            address=address,
            check_info=check_info,
            contact_email=contact_email,
            date_last_paid=date_last_paid,
            default_address=default_address,
            domestic_wire_routing_info=domestic_wire_routing_info,
            electronic_routing_info=electronic_routing_info,
            international_wire_routing_info=international_wire_routing_info,
            invite_id=invite_id,
            is_business=is_business,
            nickname=nickname,
            real_time_payment_routing_info=real_time_payment_routing_info,
        )

        recipient_info.additional_properties = d
        return recipient_info

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
