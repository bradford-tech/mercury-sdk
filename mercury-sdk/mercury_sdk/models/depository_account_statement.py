from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_statement_transaction import AccountStatementTransaction
    from ..models.address import Address


T = TypeVar("T", bound="DepositoryAccountStatement")


@_attrs_define
class DepositoryAccountStatement:
    """
    Attributes:
        account_number (str):
        company_legal_address (Address):
        company_legal_name (str):
        download_url (str):
        end_date (datetime.datetime):  Example: 2016-07-22T00:00:00Z.
        ending_balance (float): A dollar amount
        id (UUID): ID for the account statement
        routing_number (str):
        start_date (datetime.datetime):  Example: 2016-07-22T00:00:00Z.
        transactions (list[AccountStatementTransaction]):
        ein (None | str | Unset):
    """

    account_number: str
    company_legal_address: Address
    company_legal_name: str
    download_url: str
    end_date: datetime.datetime
    ending_balance: float
    id: UUID
    routing_number: str
    start_date: datetime.datetime
    transactions: list[AccountStatementTransaction]
    ein: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_number = self.account_number

        company_legal_address = self.company_legal_address.to_dict()

        company_legal_name = self.company_legal_name

        download_url = self.download_url

        end_date = self.end_date.isoformat()

        ending_balance = self.ending_balance

        id = str(self.id)

        routing_number = self.routing_number

        start_date = self.start_date.isoformat()

        transactions = []
        for transactions_item_data in self.transactions:
            transactions_item = transactions_item_data.to_dict()
            transactions.append(transactions_item)

        ein: None | str | Unset
        if isinstance(self.ein, Unset):
            ein = UNSET
        else:
            ein = self.ein

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountNumber": account_number,
                "companyLegalAddress": company_legal_address,
                "companyLegalName": company_legal_name,
                "downloadUrl": download_url,
                "endDate": end_date,
                "endingBalance": ending_balance,
                "id": id,
                "routingNumber": routing_number,
                "startDate": start_date,
                "transactions": transactions,
            }
        )
        if ein is not UNSET:
            field_dict["ein"] = ein

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_statement_transaction import AccountStatementTransaction
        from ..models.address import Address

        d = dict(src_dict)
        account_number = d.pop("accountNumber")

        company_legal_address = Address.from_dict(d.pop("companyLegalAddress"))

        company_legal_name = d.pop("companyLegalName")

        download_url = d.pop("downloadUrl")

        end_date = datetime.datetime.fromisoformat(d.pop("endDate"))

        ending_balance = d.pop("endingBalance")

        id = UUID(d.pop("id"))

        routing_number = d.pop("routingNumber")

        start_date = datetime.datetime.fromisoformat(d.pop("startDate"))

        transactions = []
        _transactions = d.pop("transactions")
        for transactions_item_data in _transactions:
            transactions_item = AccountStatementTransaction.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        def _parse_ein(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ein = _parse_ein(d.pop("ein", UNSET))

        depository_account_statement = cls(
            account_number=account_number,
            company_legal_address=company_legal_address,
            company_legal_name=company_legal_name,
            download_url=download_url,
            end_date=end_date,
            ending_balance=ending_balance,
            id=id,
            routing_number=routing_number,
            start_date=start_date,
            transactions=transactions,
            ein=ein,
        )

        depository_account_statement.additional_properties = d
        return depository_account_statement

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
