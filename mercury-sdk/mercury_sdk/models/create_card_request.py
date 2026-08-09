from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.card_kind import CardKind
from ..models.create_card_type import CreateCardType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_spend_limit import CreateSpendLimit


T = TypeVar("T", bound="CreateCardRequest")


@_attrs_define
class CreateCardRequest:
    r"""
    Attributes:
        kind (CardKind):
        type_ (CreateCardType):
        user_id (UUID):  The user to assign as the cardholder.
        account_id (None | Unset | UUID):  The account the new card will draw funds from. Required when @kind@ is
             @debit@; list available account IDs via @GET https:\/\/api.mercury.com\/api\/v1\/accounts@
             (for debit card creation, the accountId must be associated with a checking account).
             Optional when @kind@ is @credit@; omit to use your organization's Mercury
             credit account, or pass the credit accountId from @GET https:\/\/api.mercury.com\/api\/v1\/credit@.
        nickname (None | str | Unset):  Optional user-assigned label for the card.
        spend_limit (CreateSpendLimit | None | Unset):  Spending controls to apply at issuance.
    """

    kind: CardKind
    type_: CreateCardType
    user_id: UUID
    account_id: None | Unset | UUID = UNSET
    nickname: None | str | Unset = UNSET
    spend_limit: CreateSpendLimit | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_spend_limit import CreateSpendLimit

        kind = self.kind.value

        type_ = self.type_.value

        user_id = str(self.user_id)

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        elif isinstance(self.account_id, UUID):
            account_id = str(self.account_id)
        else:
            account_id = self.account_id

        nickname: None | str | Unset
        if isinstance(self.nickname, Unset):
            nickname = UNSET
        else:
            nickname = self.nickname

        spend_limit: dict[str, Any] | None | Unset
        if isinstance(self.spend_limit, Unset):
            spend_limit = UNSET
        elif isinstance(self.spend_limit, CreateSpendLimit):
            spend_limit = self.spend_limit.to_dict()
        else:
            spend_limit = self.spend_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "type": type_,
                "userId": user_id,
            }
        )
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if spend_limit is not UNSET:
            field_dict["spendLimit"] = spend_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_spend_limit import CreateSpendLimit

        d = dict(src_dict)
        kind = CardKind(d.pop("kind"))

        type_ = CreateCardType(d.pop("type"))

        user_id = UUID(d.pop("userId"))

        def _parse_account_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                account_id_type_0 = UUID(data)

                return account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))

        def _parse_nickname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nickname = _parse_nickname(d.pop("nickname", UNSET))

        def _parse_spend_limit(data: object) -> CreateSpendLimit | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                spend_limit_type_0 = CreateSpendLimit.from_dict(data)

                return spend_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateSpendLimit | None | Unset, data)

        spend_limit = _parse_spend_limit(d.pop("spendLimit", UNSET))

        create_card_request = cls(
            kind=kind,
            type_=type_,
            user_id=user_id,
            account_id=account_id,
            nickname=nickname,
            spend_limit=spend_limit,
        )

        create_card_request.additional_properties = d
        return create_card_request

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
