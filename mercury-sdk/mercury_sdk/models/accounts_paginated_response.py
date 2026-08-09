from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.accounts_paginated_response_page import AccountsPaginatedResponsePage


T = TypeVar("T", bound="AccountsPaginatedResponse")


@_attrs_define
class AccountsPaginatedResponse:
    """Paginated response containing a list of accounts.
    | Use the page cursor information to fetch additional pages of accounts.

       Attributes:
           accounts (list[Account]):  List of accounts in the current page
           page (AccountsPaginatedResponsePage):  Pagination information including cursors for navigating to next/previous
               pages
    """

    accounts: list[Account]
    page: AccountsPaginatedResponsePage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()
            accounts.append(accounts_item)

        page = self.page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts": accounts,
                "page": page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.accounts_paginated_response_page import AccountsPaginatedResponsePage

        d = dict(src_dict)
        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in _accounts:
            accounts_item = Account.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        page = AccountsPaginatedResponsePage.from_dict(d.pop("page"))

        accounts_paginated_response = cls(
            accounts=accounts,
            page=page,
        )

        accounts_paginated_response.additional_properties = d
        return accounts_paginated_response

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
