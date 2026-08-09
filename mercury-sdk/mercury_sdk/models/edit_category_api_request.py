from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditCategoryApiRequest")


@_attrs_define
class EditCategoryApiRequest:
    """Request body for editing an existing expense category. All fields are optional.

    Attributes:
        name (None | str | Unset):  New name for the category
        visible_for_card_spend (bool | None | Unset):  Whether this category is applicable to card transactions
        visible_for_other (bool | None | Unset):  Whether this category is applicable to all other transaction kinds
        visible_for_reimbursements (bool | None | Unset):  Whether this category is applicable to expense reimbursement
            transactions
    """

    name: None | str | Unset = UNSET
    visible_for_card_spend: bool | None | Unset = UNSET
    visible_for_other: bool | None | Unset = UNSET
    visible_for_reimbursements: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        visible_for_card_spend: bool | None | Unset
        if isinstance(self.visible_for_card_spend, Unset):
            visible_for_card_spend = UNSET
        else:
            visible_for_card_spend = self.visible_for_card_spend

        visible_for_other: bool | None | Unset
        if isinstance(self.visible_for_other, Unset):
            visible_for_other = UNSET
        else:
            visible_for_other = self.visible_for_other

        visible_for_reimbursements: bool | None | Unset
        if isinstance(self.visible_for_reimbursements, Unset):
            visible_for_reimbursements = UNSET
        else:
            visible_for_reimbursements = self.visible_for_reimbursements

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if visible_for_card_spend is not UNSET:
            field_dict["visibleForCardSpend"] = visible_for_card_spend
        if visible_for_other is not UNSET:
            field_dict["visibleForOther"] = visible_for_other
        if visible_for_reimbursements is not UNSET:
            field_dict["visibleForReimbursements"] = visible_for_reimbursements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_visible_for_card_spend(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        visible_for_card_spend = _parse_visible_for_card_spend(d.pop("visibleForCardSpend", UNSET))

        def _parse_visible_for_other(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        visible_for_other = _parse_visible_for_other(d.pop("visibleForOther", UNSET))

        def _parse_visible_for_reimbursements(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        visible_for_reimbursements = _parse_visible_for_reimbursements(d.pop("visibleForReimbursements", UNSET))

        edit_category_api_request = cls(
            name=name,
            visible_for_card_spend=visible_for_card_spend,
            visible_for_other=visible_for_other,
            visible_for_reimbursements=visible_for_reimbursements,
        )

        edit_category_api_request.additional_properties = d
        return edit_category_api_request

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
