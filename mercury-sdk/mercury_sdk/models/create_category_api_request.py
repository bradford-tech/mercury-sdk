from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateCategoryApiRequest")


@_attrs_define
class CreateCategoryApiRequest:
    """Request body for creating a new expense category

    Attributes:
        name (str):  Name of the category
        visible_for_card_spend (bool):  Whether this category is applicable to card transactions
        visible_for_other (bool):  Whether this category is applicable to all other transaction kinds
        visible_for_reimbursements (bool):  Whether this category is applicable to expense reimbursement transactions
    """

    name: str
    visible_for_card_spend: bool
    visible_for_other: bool
    visible_for_reimbursements: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        visible_for_card_spend = self.visible_for_card_spend

        visible_for_other = self.visible_for_other

        visible_for_reimbursements = self.visible_for_reimbursements

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "visibleForCardSpend": visible_for_card_spend,
                "visibleForOther": visible_for_other,
                "visibleForReimbursements": visible_for_reimbursements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        visible_for_card_spend = d.pop("visibleForCardSpend")

        visible_for_other = d.pop("visibleForOther")

        visible_for_reimbursements = d.pop("visibleForReimbursements")

        create_category_api_request = cls(
            name=name,
            visible_for_card_spend=visible_for_card_spend,
            visible_for_other=visible_for_other,
            visible_for_reimbursements=visible_for_reimbursements,
        )

        create_category_api_request.additional_properties = d
        return create_category_api_request

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
