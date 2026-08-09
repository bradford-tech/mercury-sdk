from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_v1_ar_invoices_data import ApiV1ArInvoicesData
    from ..models.api_v1_ar_invoices_paginated_response_page import ApiV1ArInvoicesPaginatedResponsePage


T = TypeVar("T", bound="ApiV1ArInvoicesPaginatedResponse")


@_attrs_define
class ApiV1ArInvoicesPaginatedResponse:
    """Paginated response containing a list of invoices.
    | Use the page cursor information to fetch additional pages of invoices.

       Attributes:
           invoices (list[ApiV1ArInvoicesData]):  List of invoices in the current page
           page (ApiV1ArInvoicesPaginatedResponsePage):  Pagination information including cursors for navigating to
               next/previous pages
    """

    invoices: list[ApiV1ArInvoicesData]
    page: ApiV1ArInvoicesPaginatedResponsePage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invoices = []
        for invoices_item_data in self.invoices:
            invoices_item = invoices_item_data.to_dict()
            invoices.append(invoices_item)

        page = self.page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoices": invoices,
                "page": page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_ar_invoices_data import ApiV1ArInvoicesData
        from ..models.api_v1_ar_invoices_paginated_response_page import ApiV1ArInvoicesPaginatedResponsePage

        d = dict(src_dict)
        invoices = []
        _invoices = d.pop("invoices")
        for invoices_item_data in _invoices:
            invoices_item = ApiV1ArInvoicesData.from_dict(invoices_item_data)

            invoices.append(invoices_item)

        page = ApiV1ArInvoicesPaginatedResponsePage.from_dict(d.pop("page"))

        api_v1_ar_invoices_paginated_response = cls(
            invoices=invoices,
            page=page,
        )

        api_v1_ar_invoices_paginated_response.additional_properties = d
        return api_v1_ar_invoices_paginated_response

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
