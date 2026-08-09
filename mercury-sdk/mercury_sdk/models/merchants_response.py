from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.merchant_info import MerchantInfo
    from ..models.merchants_response_page import MerchantsResponsePage


T = TypeVar("T", bound="MerchantsResponse")


@_attrs_define
class MerchantsResponse:
    """Paginated response for merchants endpoint

    Attributes:
        data (list[MerchantInfo]):
        page (MerchantsResponsePage):
    """

    data: list[MerchantInfo]
    page: MerchantsResponsePage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        page = self.page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "page": page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.merchant_info import MerchantInfo
        from ..models.merchants_response_page import MerchantsResponsePage

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = MerchantInfo.from_dict(data_item_data)

            data.append(data_item)

        page = MerchantsResponsePage.from_dict(d.pop("page"))

        merchants_response = cls(
            data=data,
            page=page,
        )

        merchants_response.additional_properties = d
        return merchants_response

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
