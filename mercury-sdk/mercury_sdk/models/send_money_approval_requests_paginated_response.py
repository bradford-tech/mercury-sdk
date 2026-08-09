from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.send_money_approval_request_response import SendMoneyApprovalRequestResponse
    from ..models.send_money_approval_requests_paginated_response_page import (
        SendMoneyApprovalRequestsPaginatedResponsePage,
    )


T = TypeVar("T", bound="SendMoneyApprovalRequestsPaginatedResponse")


@_attrs_define
class SendMoneyApprovalRequestsPaginatedResponse:
    """
    Attributes:
        page (SendMoneyApprovalRequestsPaginatedResponsePage):
        requests (list[SendMoneyApprovalRequestResponse]):
    """

    page: SendMoneyApprovalRequestsPaginatedResponsePage
    requests: list[SendMoneyApprovalRequestResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page.to_dict()

        requests = []
        for requests_item_data in self.requests:
            requests_item = requests_item_data.to_dict()
            requests.append(requests_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "requests": requests,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_money_approval_request_response import SendMoneyApprovalRequestResponse
        from ..models.send_money_approval_requests_paginated_response_page import (
            SendMoneyApprovalRequestsPaginatedResponsePage,
        )

        d = dict(src_dict)
        page = SendMoneyApprovalRequestsPaginatedResponsePage.from_dict(d.pop("page"))

        requests = []
        _requests = d.pop("requests")
        for requests_item_data in _requests:
            requests_item = SendMoneyApprovalRequestResponse.from_dict(requests_item_data)

            requests.append(requests_item)

        send_money_approval_requests_paginated_response = cls(
            page=page,
            requests=requests,
        )

        send_money_approval_requests_paginated_response.additional_properties = d
        return send_money_approval_requests_paginated_response

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
