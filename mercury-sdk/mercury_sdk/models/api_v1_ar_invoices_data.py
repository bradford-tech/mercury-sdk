from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_link_status import PaymentLinkStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiV1ArInvoicesData")


@_attrs_define
class ApiV1ArInvoicesData:
    """Response data for Accounts Receivable invoices API Endpoint

    Attributes:
        ach_debit_enabled (bool):  Whether or not the invoice can be paid via ach debit.
        amount (float):  The total amount of the invoice line items plus taxes
        cc_emails (list[str]):  Emails to be CCed on invoice notifications/reminders.
        created_at (datetime.datetime):  The timestamp when the invoice was created. Example: 2016-07-22T00:00:00Z.
        credit_card_enabled (bool):  Whether or not the invoice can be paid via credit card. Requires stripe to be
             setup for the Mercury account.
        currency_code (str):  ISO 4217 currency code for the invoice (e.g. "USD", "EUR").
        customer_id (UUID):  Id of the customer the invoice was sent to.
        destination_account_id (UUID):  The Mercury account where invoice payments will be deposited. Use the
            /api/v1/accounts endpoint to list your accounts and find the corresponding id. Only checking and savings
            accounts are supported.
        due_date (datetime.date):  The due date the invoice should be paid by. Example: 2016-07-22.
        id (UUID):  The ID of the invoice.
        invoice_date (datetime.date):  The date of the invoice, set by the invoice creator
             and likely to be context specific to the type of transaction.
             i.e. it could be a date a service was performed, it does not need
             to be the date the invoice was created. Example: 2016-07-22.
        invoice_number (str):  The payer facing invoice number/identifier.
        slug (str):  A unique identifier used to build public URLs for this invoice. Use it to construct the payment
            page URL (https://app.mercury.com/pay/{slug}) or fetch the invoice PDF via /api/v1/ar/invoices/{slug}/pdf.
        status (PaymentLinkStatus):
        updated_at (datetime.datetime):  The timestamp when the invoice was updated. Example: 2016-07-22T00:00:00Z.
        use_real_account_number (bool):  Whether or not the invoice payment instructions will show the real
             account and routing number for the destination account or use
             virtual account numbers instead.
        canceled_at (datetime.datetime | None | Unset):  The time when the invoice was canceled. Example:
            2016-07-22T00:00:00Z.
        internal_note (None | str | Unset):  Internal note for the invoice, visible by users in the
             mercury organization but not visible to payers.
        payer_memo (None | str | Unset):  Memo for the payer of the invoice.
        po_number (None | str | Unset):  Purchase order number for the invoice if applicable.
    """

    ach_debit_enabled: bool
    amount: float
    cc_emails: list[str]
    created_at: datetime.datetime
    credit_card_enabled: bool
    currency_code: str
    customer_id: UUID
    destination_account_id: UUID
    due_date: datetime.date
    id: UUID
    invoice_date: datetime.date
    invoice_number: str
    slug: str
    status: PaymentLinkStatus
    updated_at: datetime.datetime
    use_real_account_number: bool
    canceled_at: datetime.datetime | None | Unset = UNSET
    internal_note: None | str | Unset = UNSET
    payer_memo: None | str | Unset = UNSET
    po_number: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ach_debit_enabled = self.ach_debit_enabled

        amount = self.amount

        cc_emails = self.cc_emails

        created_at = self.created_at.isoformat()

        credit_card_enabled = self.credit_card_enabled

        currency_code = self.currency_code

        customer_id = str(self.customer_id)

        destination_account_id = str(self.destination_account_id)

        due_date = self.due_date.isoformat()

        id = str(self.id)

        invoice_date = self.invoice_date.isoformat()

        invoice_number = self.invoice_number

        slug = self.slug

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        use_real_account_number = self.use_real_account_number

        canceled_at: None | str | Unset
        if isinstance(self.canceled_at, Unset):
            canceled_at = UNSET
        elif isinstance(self.canceled_at, datetime.datetime):
            canceled_at = self.canceled_at.isoformat()
        else:
            canceled_at = self.canceled_at

        internal_note: None | str | Unset
        if isinstance(self.internal_note, Unset):
            internal_note = UNSET
        else:
            internal_note = self.internal_note

        payer_memo: None | str | Unset
        if isinstance(self.payer_memo, Unset):
            payer_memo = UNSET
        else:
            payer_memo = self.payer_memo

        po_number: None | str | Unset
        if isinstance(self.po_number, Unset):
            po_number = UNSET
        else:
            po_number = self.po_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "achDebitEnabled": ach_debit_enabled,
                "amount": amount,
                "ccEmails": cc_emails,
                "createdAt": created_at,
                "creditCardEnabled": credit_card_enabled,
                "currencyCode": currency_code,
                "customerId": customer_id,
                "destinationAccountId": destination_account_id,
                "dueDate": due_date,
                "id": id,
                "invoiceDate": invoice_date,
                "invoiceNumber": invoice_number,
                "slug": slug,
                "status": status,
                "updatedAt": updated_at,
                "useRealAccountNumber": use_real_account_number,
            }
        )
        if canceled_at is not UNSET:
            field_dict["canceledAt"] = canceled_at
        if internal_note is not UNSET:
            field_dict["internalNote"] = internal_note
        if payer_memo is not UNSET:
            field_dict["payerMemo"] = payer_memo
        if po_number is not UNSET:
            field_dict["poNumber"] = po_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ach_debit_enabled = d.pop("achDebitEnabled")

        amount = d.pop("amount")

        cc_emails = cast(list[str], d.pop("ccEmails"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        credit_card_enabled = d.pop("creditCardEnabled")

        currency_code = d.pop("currencyCode")

        customer_id = UUID(d.pop("customerId"))

        destination_account_id = UUID(d.pop("destinationAccountId"))

        due_date = datetime.date.fromisoformat(d.pop("dueDate"))

        id = UUID(d.pop("id"))

        invoice_date = datetime.date.fromisoformat(d.pop("invoiceDate"))

        invoice_number = d.pop("invoiceNumber")

        slug = d.pop("slug")

        status = PaymentLinkStatus(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        use_real_account_number = d.pop("useRealAccountNumber")

        def _parse_canceled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                canceled_at_type_0 = datetime.datetime.fromisoformat(data)

                return canceled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        canceled_at = _parse_canceled_at(d.pop("canceledAt", UNSET))

        def _parse_internal_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_note = _parse_internal_note(d.pop("internalNote", UNSET))

        def _parse_payer_memo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payer_memo = _parse_payer_memo(d.pop("payerMemo", UNSET))

        def _parse_po_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        po_number = _parse_po_number(d.pop("poNumber", UNSET))

        api_v1_ar_invoices_data = cls(
            ach_debit_enabled=ach_debit_enabled,
            amount=amount,
            cc_emails=cc_emails,
            created_at=created_at,
            credit_card_enabled=credit_card_enabled,
            currency_code=currency_code,
            customer_id=customer_id,
            destination_account_id=destination_account_id,
            due_date=due_date,
            id=id,
            invoice_date=invoice_date,
            invoice_number=invoice_number,
            slug=slug,
            status=status,
            updated_at=updated_at,
            use_real_account_number=use_real_account_number,
            canceled_at=canceled_at,
            internal_note=internal_note,
            payer_memo=payer_memo,
            po_number=po_number,
        )

        api_v1_ar_invoices_data.additional_properties = d
        return api_v1_ar_invoices_data

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
