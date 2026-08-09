from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_status import AccountStatus
from ..models.account_type import AccountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """
    Attributes:
        account_number (str):
        available_balance (float):
        created_at (datetime.datetime):  Example: 2016-07-22T00:00:00Z.
        current_balance (float):
        dashboard_link (str):
        id (UUID): ID for a Mercury account.
        kind (str):
        legal_business_name (str):
        name (str):
        routing_number (str):
        status (AccountStatus):
        type_ (AccountType):
        can_receive_transactions (bool | None | Unset):
        nickname (None | str | Unset):
    """

    account_number: str
    available_balance: float
    created_at: datetime.datetime
    current_balance: float
    dashboard_link: str
    id: UUID
    kind: str
    legal_business_name: str
    name: str
    routing_number: str
    status: AccountStatus
    type_: AccountType
    can_receive_transactions: bool | None | Unset = UNSET
    nickname: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_number = self.account_number

        available_balance = self.available_balance

        created_at = self.created_at.isoformat()

        current_balance = self.current_balance

        dashboard_link = self.dashboard_link

        id = str(self.id)

        kind = self.kind

        legal_business_name = self.legal_business_name

        name = self.name

        routing_number = self.routing_number

        status = self.status.value

        type_ = self.type_.value

        can_receive_transactions: bool | None | Unset
        if isinstance(self.can_receive_transactions, Unset):
            can_receive_transactions = UNSET
        else:
            can_receive_transactions = self.can_receive_transactions

        nickname: None | str | Unset
        if isinstance(self.nickname, Unset):
            nickname = UNSET
        else:
            nickname = self.nickname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountNumber": account_number,
                "availableBalance": available_balance,
                "createdAt": created_at,
                "currentBalance": current_balance,
                "dashboardLink": dashboard_link,
                "id": id,
                "kind": kind,
                "legalBusinessName": legal_business_name,
                "name": name,
                "routingNumber": routing_number,
                "status": status,
                "type": type_,
            }
        )
        if can_receive_transactions is not UNSET:
            field_dict["canReceiveTransactions"] = can_receive_transactions
        if nickname is not UNSET:
            field_dict["nickname"] = nickname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_number = d.pop("accountNumber")

        available_balance = d.pop("availableBalance")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        current_balance = d.pop("currentBalance")

        dashboard_link = d.pop("dashboardLink")

        id = UUID(d.pop("id"))

        kind = d.pop("kind")

        legal_business_name = d.pop("legalBusinessName")

        name = d.pop("name")

        routing_number = d.pop("routingNumber")

        status = AccountStatus(d.pop("status"))

        type_ = AccountType(d.pop("type"))

        def _parse_can_receive_transactions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_receive_transactions = _parse_can_receive_transactions(d.pop("canReceiveTransactions", UNSET))

        def _parse_nickname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nickname = _parse_nickname(d.pop("nickname", UNSET))

        account = cls(
            account_number=account_number,
            available_balance=available_balance,
            created_at=created_at,
            current_balance=current_balance,
            dashboard_link=dashboard_link,
            id=id,
            kind=kind,
            legal_business_name=legal_business_name,
            name=name,
            routing_number=routing_number,
            status=status,
            type_=type_,
            can_receive_transactions=can_receive_transactions,
            nickname=nickname,
        )

        account.additional_properties = d
        return account

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
