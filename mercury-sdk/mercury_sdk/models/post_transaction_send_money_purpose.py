from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.simple_purpose import SimplePurpose


T = TypeVar("T", bound="PostTransactionSendMoneyPurpose")


@_attrs_define
class PostTransactionSendMoneyPurpose:
    """External API representation of SendMoneyPurpose.
    Only exposes the 'simple' field to decouple internal implementation from external API.

       Attributes:
           simple (None | SimplePurpose | Unset):
    """

    simple: None | SimplePurpose | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.simple_purpose import SimplePurpose

        simple: dict[str, Any] | None | Unset
        if isinstance(self.simple, Unset):
            simple = UNSET
        elif isinstance(self.simple, SimplePurpose):
            simple = self.simple.to_dict()
        else:
            simple = self.simple

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if simple is not UNSET:
            field_dict["simple"] = simple

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_purpose import SimplePurpose

        d = dict(src_dict)

        def _parse_simple(data: object) -> None | SimplePurpose | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                simple_type_0 = SimplePurpose.from_dict(data)

                return simple_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SimplePurpose | Unset, data)

        simple = _parse_simple(d.pop("simple", UNSET))

        post_transaction_send_money_purpose = cls(
            simple=simple,
        )

        post_transaction_send_money_purpose.additional_properties = d
        return post_transaction_send_money_purpose

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
