from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_v1_ar_customer_paginated_response_data_page import ApiV1ArCustomerPaginatedResponseDataPage
    from ..models.api_v1_ar_customer_response_data import ApiV1ArCustomerResponseData


T = TypeVar("T", bound="ApiV1ArCustomerPaginatedResponseData")


@_attrs_define
class ApiV1ArCustomerPaginatedResponseData:
    """Paginated response data for Accounts Receivable customers API endpoint

    Attributes:
        customers (list[ApiV1ArCustomerResponseData]):  The list of customers for this page
        page (ApiV1ArCustomerPaginatedResponseDataPage):  Pagination cursors for navigating to next/previous pages
    """

    customers: list[ApiV1ArCustomerResponseData]
    page: ApiV1ArCustomerPaginatedResponseDataPage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customers = []
        for customers_item_data in self.customers:
            customers_item = customers_item_data.to_dict()
            customers.append(customers_item)

        page = self.page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customers": customers,
                "page": page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_ar_customer_paginated_response_data_page import ApiV1ArCustomerPaginatedResponseDataPage
        from ..models.api_v1_ar_customer_response_data import ApiV1ArCustomerResponseData

        d = dict(src_dict)
        customers = []
        _customers = d.pop("customers")
        for customers_item_data in _customers:
            customers_item = ApiV1ArCustomerResponseData.from_dict(customers_item_data)

            customers.append(customers_item)

        page = ApiV1ArCustomerPaginatedResponseDataPage.from_dict(d.pop("page"))

        api_v1_ar_customer_paginated_response_data = cls(
            customers=customers,
            page=page,
        )

        api_v1_ar_customer_paginated_response_data.additional_properties = d
        return api_v1_ar_customer_paginated_response_data

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
