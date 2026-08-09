from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transaction import Transaction
    from ..models.transactions_paginated_response_page import TransactionsPaginatedResponsePage


T = TypeVar("T", bound="TransactionsPaginatedResponse")


@_attrs_define
class TransactionsPaginatedResponse:
    """
    Attributes:
        page (TransactionsPaginatedResponsePage):
        transactions (list[Transaction]):
    """

    page: TransactionsPaginatedResponsePage
    transactions: list[Transaction]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page.to_dict()

        transactions = []
        for transactions_item_data in self.transactions:
            transactions_item = transactions_item_data.to_dict()
            transactions.append(transactions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "transactions": transactions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction import Transaction
        from ..models.transactions_paginated_response_page import TransactionsPaginatedResponsePage

        d = dict(src_dict)
        page = TransactionsPaginatedResponsePage.from_dict(d.pop("page"))

        transactions = []
        _transactions = d.pop("transactions")
        for transactions_item_data in _transactions:
            transactions_item = Transaction.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        transactions_paginated_response = cls(
            page=page,
            transactions=transactions,
        )

        transactions_paginated_response.additional_properties = d
        return transactions_paginated_response

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
