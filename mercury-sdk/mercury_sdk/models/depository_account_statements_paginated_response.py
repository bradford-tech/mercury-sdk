from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.depository_account_statement import DepositoryAccountStatement
    from ..models.depository_account_statements_paginated_response_page import (
        DepositoryAccountStatementsPaginatedResponsePage,
    )


T = TypeVar("T", bound="DepositoryAccountStatementsPaginatedResponse")


@_attrs_define
class DepositoryAccountStatementsPaginatedResponse:
    """Paginated response for depository account statements (v1 API)

    Attributes:
        page (DepositoryAccountStatementsPaginatedResponsePage):
        statements (list[DepositoryAccountStatement]):
    """

    page: DepositoryAccountStatementsPaginatedResponsePage
    statements: list[DepositoryAccountStatement]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page.to_dict()

        statements = []
        for statements_item_data in self.statements:
            statements_item = statements_item_data.to_dict()
            statements.append(statements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "statements": statements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.depository_account_statement import DepositoryAccountStatement
        from ..models.depository_account_statements_paginated_response_page import (
            DepositoryAccountStatementsPaginatedResponsePage,
        )

        d = dict(src_dict)
        page = DepositoryAccountStatementsPaginatedResponsePage.from_dict(d.pop("page"))

        statements = []
        _statements = d.pop("statements")
        for statements_item_data in _statements:
            statements_item = DepositoryAccountStatement.from_dict(statements_item_data)

            statements.append(statements_item)

        depository_account_statements_paginated_response = cls(
            page=page,
            statements=statements,
        )

        depository_account_statements_paginated_response.additional_properties = d
        return depository_account_statements_paginated_response

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
