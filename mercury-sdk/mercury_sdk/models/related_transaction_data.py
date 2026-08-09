from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transaction_relation_kind import TransactionRelationKind

T = TypeVar("T", bound="RelatedTransactionData")


@_attrs_define
class RelatedTransactionData:
    """A Public API version of RelatedTransactionData.

    Attributes:
        account_id (UUID): ID for a Mercury account.
        amount (float):
        id (UUID): ID for this transaction
        relation_kind (TransactionRelationKind):
    """

    account_id: UUID
    amount: float
    id: UUID
    relation_kind: TransactionRelationKind
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = str(self.account_id)

        amount = self.amount

        id = str(self.id)

        relation_kind = self.relation_kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "amount": amount,
                "id": id,
                "relationKind": relation_kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = UUID(d.pop("accountId"))

        amount = d.pop("amount")

        id = UUID(d.pop("id"))

        relation_kind = TransactionRelationKind(d.pop("relationKind"))

        related_transaction_data = cls(
            account_id=account_id,
            amount=amount,
            id=id,
            relation_kind=relation_kind,
        )

        related_transaction_data.additional_properties = d
        return related_transaction_data

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
