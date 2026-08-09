from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.categories_paginated_response_page import CategoriesPaginatedResponsePage
    from ..models.category_data import CategoryData


T = TypeVar("T", bound="CategoriesPaginatedResponse")


@_attrs_define
class CategoriesPaginatedResponse:
    """Paginated response containing a list of categories.
    | Use the page cursor information to fetch additional pages of categories.

       Attributes:
           categories (list[CategoryData]):  List of categories in the current page
           page (CategoriesPaginatedResponsePage):  Pagination information including cursors for navigating to
               next/previous pages
    """

    categories: list[CategoryData]
    page: CategoriesPaginatedResponsePage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        page = self.page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "categories": categories,
                "page": page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.categories_paginated_response_page import CategoriesPaginatedResponsePage
        from ..models.category_data import CategoryData

        d = dict(src_dict)
        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = CategoryData.from_dict(categories_item_data)

            categories.append(categories_item)

        page = CategoriesPaginatedResponsePage.from_dict(d.pop("page"))

        categories_paginated_response = cls(
            categories=categories,
            page=page,
        )

        categories_paginated_response.additional_properties = d
        return categories_paginated_response

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
