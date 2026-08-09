from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_webhook_response import ApiWebhookResponse
    from ..models.api_webhooks_paginated_response_page import ApiWebhooksPaginatedResponsePage


T = TypeVar("T", bound="ApiWebhooksPaginatedResponse")


@_attrs_define
class ApiWebhooksPaginatedResponse:
    """API response for listing webhook endpoints with pagination

    Attributes:
        page (ApiWebhooksPaginatedResponsePage):  Pagination information including cursors for navigating to
            next/previous pages
        webhooks (list[ApiWebhookResponse]):  List of webhooks in the current page
    """

    page: ApiWebhooksPaginatedResponsePage
    webhooks: list[ApiWebhookResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page.to_dict()

        webhooks = []
        for webhooks_item_data in self.webhooks:
            webhooks_item = webhooks_item_data.to_dict()
            webhooks.append(webhooks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "webhooks": webhooks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_webhook_response import ApiWebhookResponse
        from ..models.api_webhooks_paginated_response_page import ApiWebhooksPaginatedResponsePage

        d = dict(src_dict)
        page = ApiWebhooksPaginatedResponsePage.from_dict(d.pop("page"))

        webhooks = []
        _webhooks = d.pop("webhooks")
        for webhooks_item_data in _webhooks:
            webhooks_item = ApiWebhookResponse.from_dict(webhooks_item_data)

            webhooks.append(webhooks_item)

        api_webhooks_paginated_response = cls(
            page=page,
            webhooks=webhooks,
        )

        api_webhooks_paginated_response.additional_properties = d
        return api_webhooks_paginated_response

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
