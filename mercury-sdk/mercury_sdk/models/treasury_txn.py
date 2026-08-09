from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.treasury_transaction_type import TreasuryTransactionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.treasury_transaction_details import TreasuryTransactionDetails


T = TypeVar("T", bound="TreasuryTxn")


@_attrs_define
class TreasuryTxn:
    """Treasury transaction data for external API consumption

    Attributes:
        account_id (UUID): ID for a Mercury account.
        amount (float):
        balance (float):
        canonical_day (datetime.date):  Example: 2016-07-22.
        description (str):
        id (UUID): ID for this treasury transaction
        type_ (TreasuryTransactionType):
        additional_details (None | str | Unset):
        details (None | TreasuryTransactionDetails | Unset):
        security (None | str | Unset):
    """

    account_id: UUID
    amount: float
    balance: float
    canonical_day: datetime.date
    description: str
    id: UUID
    type_: TreasuryTransactionType
    additional_details: None | str | Unset = UNSET
    details: None | TreasuryTransactionDetails | Unset = UNSET
    security: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.treasury_transaction_details import TreasuryTransactionDetails

        account_id = str(self.account_id)

        amount = self.amount

        balance = self.balance

        canonical_day = self.canonical_day.isoformat()

        description = self.description

        id = str(self.id)

        type_ = self.type_.value

        additional_details: None | str | Unset
        if isinstance(self.additional_details, Unset):
            additional_details = UNSET
        else:
            additional_details = self.additional_details

        details: dict[str, Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, TreasuryTransactionDetails):
            details = self.details.to_dict()
        else:
            details = self.details

        security: None | str | Unset
        if isinstance(self.security, Unset):
            security = UNSET
        else:
            security = self.security

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "amount": amount,
                "balance": balance,
                "canonicalDay": canonical_day,
                "description": description,
                "id": id,
                "type": type_,
            }
        )
        if additional_details is not UNSET:
            field_dict["additionalDetails"] = additional_details
        if details is not UNSET:
            field_dict["details"] = details
        if security is not UNSET:
            field_dict["security"] = security

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.treasury_transaction_details import TreasuryTransactionDetails

        d = dict(src_dict)
        account_id = UUID(d.pop("accountId"))

        amount = d.pop("amount")

        balance = d.pop("balance")

        canonical_day = datetime.date.fromisoformat(d.pop("canonicalDay"))

        description = d.pop("description")

        id = UUID(d.pop("id"))

        type_ = TreasuryTransactionType(d.pop("type"))

        def _parse_additional_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        additional_details = _parse_additional_details(d.pop("additionalDetails", UNSET))

        def _parse_details(data: object) -> None | TreasuryTransactionDetails | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = TreasuryTransactionDetails.from_dict(data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TreasuryTransactionDetails | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        def _parse_security(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        security = _parse_security(d.pop("security", UNSET))

        treasury_txn = cls(
            account_id=account_id,
            amount=amount,
            balance=balance,
            canonical_day=canonical_day,
            description=description,
            id=id,
            type_=type_,
            additional_details=additional_details,
            details=details,
            security=security,
        )

        treasury_txn.additional_properties = d
        return treasury_txn

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
