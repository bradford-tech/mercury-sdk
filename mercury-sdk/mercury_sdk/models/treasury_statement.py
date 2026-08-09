from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.treasury_statement_document_type import TreasuryStatementDocumentType

T = TypeVar("T", bound="TreasuryStatement")


@_attrs_define
class TreasuryStatement:
    """Individual treasury statement in the response

    Attributes:
        account_id (UUID):  External treasury account ID this statement belongs to
        created_at (datetime.datetime):  Timestamp when the record was created Example: 2016-07-22T00:00:00Z.
        creation_date (datetime.datetime):  Date the statement was created by the custodian Example:
            2016-07-22T00:00:00Z.
        description (str):  Human-readable description of the statement
        document_type (TreasuryStatementDocumentType):
        download_url (str):  URL to download the statement PDF
        id (UUID):  Unique identifier for the statement
        period_end (datetime.date):  End of the period covered by the statement Example: 2016-07-22.
        period_start (datetime.date):  Start of the period covered by the statement Example: 2016-07-22.
        updated_at (datetime.datetime):  Timestamp when the record was last updated Example: 2016-07-22T00:00:00Z.
    """

    account_id: UUID
    created_at: datetime.datetime
    creation_date: datetime.datetime
    description: str
    document_type: TreasuryStatementDocumentType
    download_url: str
    id: UUID
    period_end: datetime.date
    period_start: datetime.date
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = str(self.account_id)

        created_at = self.created_at.isoformat()

        creation_date = self.creation_date.isoformat()

        description = self.description

        document_type = self.document_type.value

        download_url = self.download_url

        id = str(self.id)

        period_end = self.period_end.isoformat()

        period_start = self.period_start.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "createdAt": created_at,
                "creationDate": creation_date,
                "description": description,
                "documentType": document_type,
                "downloadUrl": download_url,
                "id": id,
                "periodEnd": period_end,
                "periodStart": period_start,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = UUID(d.pop("accountId"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        creation_date = datetime.datetime.fromisoformat(d.pop("creationDate"))

        description = d.pop("description")

        document_type = TreasuryStatementDocumentType(d.pop("documentType"))

        download_url = d.pop("downloadUrl")

        id = UUID(d.pop("id"))

        period_end = datetime.date.fromisoformat(d.pop("periodEnd"))

        period_start = datetime.date.fromisoformat(d.pop("periodStart"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        treasury_statement = cls(
            account_id=account_id,
            created_at=created_at,
            creation_date=creation_date,
            description=description,
            document_type=document_type,
            download_url=download_url,
            id=id,
            period_end=period_end,
            period_start=period_start,
            updated_at=updated_at,
        )

        treasury_statement.additional_properties = d
        return treasury_statement

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
