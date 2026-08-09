from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.card_kind import CardKind
from ..models.card_status import CardStatus
from ..models.card_type import CardType
from ..models.mercury_category import MercuryCategory
from ..models.physical_card_status import PhysicalCardStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_expiration import CardExpiration
    from ..models.merchant_info import MerchantInfo
    from ..models.spend_limit import SpendLimit


T = TypeVar("T", bound="Card")


@_attrs_define
class Card:
    """
    Attributes:
        account_id (str):  The Mercury account this card is associated with.
        category_locks (list[MercuryCategory]):  Mercury spend-category locks applied to this card, in no particular
            order. Empty when the card has no category restrictions.
        created_at (datetime.datetime):  Timestamp when the card was issued. Example: 2016-07-22T00:00:00Z.
        expiration (CardExpiration): Month and year the card expires.
        id (UUID):  Unique identifier for the card.
        kind (CardKind):
        last_four (str):  Last four digits of the card's primary account number (PAN).
        name_on_card (str):  Cardholder name printed on the card.
        status (CardStatus):
        type_ (CardType):
        updated_at (datetime.datetime):  Timestamp of the last modification to the card or its settings. Example:
            2016-07-22T00:00:00Z.
        user_id (str):  Mercury User who owns the card.
        merchant_lock (MerchantInfo | None | Unset):  Merchant lock applied to this card. Present only when the card is
            locked to a single merchant; otherwise omitted.
        nickname (None | str | Unset):  Optional user-assigned label for the card.
        physical_card_status (None | PhysicalCardStatus | Unset):  Activation state of a physical card. Null for virtual
            cards.
        spend_limit (None | SpendLimit | Unset):  Card-level spending controls. Omitted when budgets govern this card.
    """

    account_id: str
    category_locks: list[MercuryCategory]
    created_at: datetime.datetime
    expiration: CardExpiration
    id: UUID
    kind: CardKind
    last_four: str
    name_on_card: str
    status: CardStatus
    type_: CardType
    updated_at: datetime.datetime
    user_id: str
    merchant_lock: MerchantInfo | None | Unset = UNSET
    nickname: None | str | Unset = UNSET
    physical_card_status: None | PhysicalCardStatus | Unset = UNSET
    spend_limit: None | SpendLimit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.merchant_info import MerchantInfo
        from ..models.spend_limit import SpendLimit

        account_id = self.account_id

        category_locks = []
        for category_locks_item_data in self.category_locks:
            category_locks_item = category_locks_item_data.value
            category_locks.append(category_locks_item)

        created_at = self.created_at.isoformat()

        expiration = self.expiration.to_dict()

        id = str(self.id)

        kind = self.kind.value

        last_four = self.last_four

        name_on_card = self.name_on_card

        status = self.status.value

        type_ = self.type_.value

        updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        merchant_lock: dict[str, Any] | None | Unset
        if isinstance(self.merchant_lock, Unset):
            merchant_lock = UNSET
        elif isinstance(self.merchant_lock, MerchantInfo):
            merchant_lock = self.merchant_lock.to_dict()
        else:
            merchant_lock = self.merchant_lock

        nickname: None | str | Unset
        if isinstance(self.nickname, Unset):
            nickname = UNSET
        else:
            nickname = self.nickname

        physical_card_status: None | str | Unset
        if isinstance(self.physical_card_status, Unset):
            physical_card_status = UNSET
        elif isinstance(self.physical_card_status, PhysicalCardStatus):
            physical_card_status = self.physical_card_status.value
        else:
            physical_card_status = self.physical_card_status

        spend_limit: dict[str, Any] | None | Unset
        if isinstance(self.spend_limit, Unset):
            spend_limit = UNSET
        elif isinstance(self.spend_limit, SpendLimit):
            spend_limit = self.spend_limit.to_dict()
        else:
            spend_limit = self.spend_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "categoryLocks": category_locks,
                "createdAt": created_at,
                "expiration": expiration,
                "id": id,
                "kind": kind,
                "lastFour": last_four,
                "nameOnCard": name_on_card,
                "status": status,
                "type": type_,
                "updatedAt": updated_at,
                "userId": user_id,
            }
        )
        if merchant_lock is not UNSET:
            field_dict["merchantLock"] = merchant_lock
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if physical_card_status is not UNSET:
            field_dict["physicalCardStatus"] = physical_card_status
        if spend_limit is not UNSET:
            field_dict["spendLimit"] = spend_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_expiration import CardExpiration
        from ..models.merchant_info import MerchantInfo
        from ..models.spend_limit import SpendLimit

        d = dict(src_dict)
        account_id = d.pop("accountId")

        category_locks = []
        _category_locks = d.pop("categoryLocks")
        for category_locks_item_data in _category_locks:
            category_locks_item = MercuryCategory(category_locks_item_data)

            category_locks.append(category_locks_item)

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        expiration = CardExpiration.from_dict(d.pop("expiration"))

        id = UUID(d.pop("id"))

        kind = CardKind(d.pop("kind"))

        last_four = d.pop("lastFour")

        name_on_card = d.pop("nameOnCard")

        status = CardStatus(d.pop("status"))

        type_ = CardType(d.pop("type"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        user_id = d.pop("userId")

        def _parse_merchant_lock(data: object) -> MerchantInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                merchant_lock_type_0 = MerchantInfo.from_dict(data)

                return merchant_lock_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MerchantInfo | None | Unset, data)

        merchant_lock = _parse_merchant_lock(d.pop("merchantLock", UNSET))

        def _parse_nickname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nickname = _parse_nickname(d.pop("nickname", UNSET))

        def _parse_physical_card_status(data: object) -> None | PhysicalCardStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                physical_card_status_type_0 = PhysicalCardStatus(data)

                return physical_card_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PhysicalCardStatus | Unset, data)

        physical_card_status = _parse_physical_card_status(d.pop("physicalCardStatus", UNSET))

        def _parse_spend_limit(data: object) -> None | SpendLimit | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                spend_limit_type_0 = SpendLimit.from_dict(data)

                return spend_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SpendLimit | Unset, data)

        spend_limit = _parse_spend_limit(d.pop("spendLimit", UNSET))

        card = cls(
            account_id=account_id,
            category_locks=category_locks,
            created_at=created_at,
            expiration=expiration,
            id=id,
            kind=kind,
            last_four=last_four,
            name_on_card=name_on_card,
            status=status,
            type_=type_,
            updated_at=updated_at,
            user_id=user_id,
            merchant_lock=merchant_lock,
            nickname=nickname,
            physical_card_status=physical_card_status,
            spend_limit=spend_limit,
        )

        card.additional_properties = d
        return card

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
