from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transaction import Transaction


T = TypeVar("T", bound="InternalTransferAPIResponse")


@_attrs_define
class InternalTransferAPIResponse:
    """Response for POST /api/v1/transfer endpoint.
    Returns both the credit and debit transactions for the transfer (depository, treasury, or investment).

       Attributes:
           credit_transaction (Transaction):
           debit_transaction (Transaction):
    """

    credit_transaction: Transaction
    debit_transaction: Transaction
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credit_transaction = self.credit_transaction.to_dict()

        debit_transaction = self.debit_transaction.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creditTransaction": credit_transaction,
                "debitTransaction": debit_transaction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction import Transaction

        d = dict(src_dict)
        credit_transaction = Transaction.from_dict(d.pop("creditTransaction"))

        debit_transaction = Transaction.from_dict(d.pop("debitTransaction"))

        internal_transfer_api_response = cls(
            credit_transaction=credit_transaction,
            debit_transaction=debit_transaction,
        )

        internal_transfer_api_response.additional_properties = d
        return internal_transfer_api_response

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
