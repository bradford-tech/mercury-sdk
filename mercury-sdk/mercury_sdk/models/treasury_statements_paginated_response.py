from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.treasury_statement import TreasuryStatement
    from ..models.treasury_statements_paginated_response_page import TreasuryStatementsPaginatedResponsePage


T = TypeVar("T", bound="TreasuryStatementsPaginatedResponse")


@_attrs_define
class TreasuryStatementsPaginatedResponse:
    """Paginated response for treasury account statements

    Attributes:
        page (TreasuryStatementsPaginatedResponsePage):
        statements (list[TreasuryStatement]):
    """

    page: TreasuryStatementsPaginatedResponsePage
    statements: list[TreasuryStatement]
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
        from ..models.treasury_statement import TreasuryStatement
        from ..models.treasury_statements_paginated_response_page import TreasuryStatementsPaginatedResponsePage

        d = dict(src_dict)
        page = TreasuryStatementsPaginatedResponsePage.from_dict(d.pop("page"))

        statements = []
        _statements = d.pop("statements")
        for statements_item_data in _statements:
            statements_item = TreasuryStatement.from_dict(statements_item_data)

            statements.append(statements_item)

        treasury_statements_paginated_response = cls(
            page=page,
            statements=statements,
        )

        treasury_statements_paginated_response.additional_properties = d
        return treasury_statements_paginated_response

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
