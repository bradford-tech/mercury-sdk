from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.card_network import CardNetwork
from ..models.card_status import CardStatus
from ..models.card_type import CardType
from ..models.physical_card_status import PhysicalCardStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spend_limit import SpendLimit


T = TypeVar("T", bound="AccountCard")


@_attrs_define
class AccountCard:
    r"""Deprecated account card representation, used by the @/v1/account\/:id\/cards@ endpoint.

    Attributes:
        card_id (str):
        created_at (datetime.datetime):  Example: 2016-07-22T00:00:00Z.
        last_four_digits (str):
        name_on_card (str):
        network (CardNetwork):
        spend_limit (SpendLimit):  Spending controls applied to a card
        status (CardStatus):
        type_ (CardType):
        updated_at (datetime.datetime):  Example: 2016-07-22T00:00:00Z.
        user_id (str):
        physical_card_status (None | PhysicalCardStatus | Unset):
    """

    card_id: str
    created_at: datetime.datetime
    last_four_digits: str
    name_on_card: str
    network: CardNetwork
    spend_limit: SpendLimit
    status: CardStatus
    type_: CardType
    updated_at: datetime.datetime
    user_id: str
    physical_card_status: None | PhysicalCardStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_id = self.card_id

        created_at = self.created_at.isoformat()

        last_four_digits = self.last_four_digits

        name_on_card = self.name_on_card

        network = self.network.value

        spend_limit = self.spend_limit.to_dict()

        status = self.status.value

        type_ = self.type_.value

        updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        physical_card_status: None | str | Unset
        if isinstance(self.physical_card_status, Unset):
            physical_card_status = UNSET
        elif isinstance(self.physical_card_status, PhysicalCardStatus):
            physical_card_status = self.physical_card_status.value
        else:
            physical_card_status = self.physical_card_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cardId": card_id,
                "createdAt": created_at,
                "lastFourDigits": last_four_digits,
                "nameOnCard": name_on_card,
                "network": network,
                "spendLimit": spend_limit,
                "status": status,
                "type": type_,
                "updatedAt": updated_at,
                "userId": user_id,
            }
        )
        if physical_card_status is not UNSET:
            field_dict["physicalCardStatus"] = physical_card_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spend_limit import SpendLimit

        d = dict(src_dict)
        card_id = d.pop("cardId")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        last_four_digits = d.pop("lastFourDigits")

        name_on_card = d.pop("nameOnCard")

        network = CardNetwork(d.pop("network"))

        spend_limit = SpendLimit.from_dict(d.pop("spendLimit"))

        status = CardStatus(d.pop("status"))

        type_ = CardType(d.pop("type"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        user_id = d.pop("userId")

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

        account_card = cls(
            card_id=card_id,
            created_at=created_at,
            last_four_digits=last_four_digits,
            name_on_card=name_on_card,
            network=network,
            spend_limit=spend_limit,
            status=status,
            type_=type_,
            updated_at=updated_at,
            user_id=user_id,
            physical_card_status=physical_card_status,
        )

        account_card.additional_properties = d
        return account_card

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
