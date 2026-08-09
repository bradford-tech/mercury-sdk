from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.treasury_txn import TreasuryTxn


T = TypeVar("T", bound="TreasuryTransactionsResponse")


@_attrs_define
class TreasuryTransactionsResponse:
    """Response type for treasury transactions API endpoint

    Attributes:
        transactions (list[TreasuryTxn]):  List of treasury transactions in the response
        cursor (int | None | Unset):  Pagination cursor for retrieving next batch of transactions
    """

    transactions: list[TreasuryTxn]
    cursor: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transactions = []
        for transactions_item_data in self.transactions:
            transactions_item = transactions_item_data.to_dict()
            transactions.append(transactions_item)

        cursor: int | None | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transactions": transactions,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.treasury_txn import TreasuryTxn

        d = dict(src_dict)
        transactions = []
        _transactions = d.pop("transactions")
        for transactions_item_data in _transactions:
            transactions_item = TreasuryTxn.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        def _parse_cursor(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        treasury_transactions_response = cls(
            transactions=transactions,
            cursor=cursor,
        )

        treasury_transactions_response.additional_properties = d
        return treasury_transactions_response

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
