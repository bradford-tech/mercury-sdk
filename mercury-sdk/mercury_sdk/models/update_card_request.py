from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spend_limit import SpendLimit


T = TypeVar("T", bound="UpdateCardRequest")


@_attrs_define
class UpdateCardRequest:
    """At least one updateable field must be provided;
    requests where every field is the same are rejected.

       Attributes:
           nickname (None | str):  Updated card nickname. Omit to keep current, send null/empty to clear, send a string to
               set.
           spend_limit (None | SpendLimit | Unset):  Updated spending controls for the card. Omit to leave unchanged.
    """

    nickname: None | str
    spend_limit: None | SpendLimit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.spend_limit import SpendLimit

        nickname: None | str
        nickname = self.nickname

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
                "nickname": nickname,
            }
        )
        if spend_limit is not UNSET:
            field_dict["spendLimit"] = spend_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spend_limit import SpendLimit

        d = dict(src_dict)

        def _parse_nickname(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        nickname = _parse_nickname(d.pop("nickname"))

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

        update_card_request = cls(
            nickname=nickname,
            spend_limit=spend_limit,
        )

        update_card_request.additional_properties = d
        return update_card_request

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
