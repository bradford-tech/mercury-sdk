from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_send_email_option import ApiSendEmailOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_v1_ar_line_item_data import ApiV1ArLineItemData


T = TypeVar("T", bound="ApiV1ArInvoiceCreateRequest")


@_attrs_define
class ApiV1ArInvoiceCreateRequest:
    """The request body to create an invoice.

    Attributes:
        ach_debit_enabled (bool):  Whether or not the invoice can be paid via ACH debit.
        cc_emails (list[str]):  Emails to be CCed on invoice notifications/reminders.
        credit_card_enabled (bool):  Whether or not the invoice can be paid via credit card. Requires Stripe to be setup
            for the Mercury account.
        customer_id (UUID):  Id of the customer the invoice was sent to.
        destination_account_id (UUID):  The Mercury account where invoice payments will be deposited. Use the
            /api/v1/accounts endpoint to list your accounts and find the corresponding id. Only checking and savings
            accounts are supported.
        due_date (datetime.date):  The due date the invoice should be paid by. YYYY-MM-DD Example: 2016-07-22.
        invoice_date (datetime.date):  The date of the invoice, set by the invoice creator and likely to be context
            specific to the type of transaction. For example, it could be a date a service was performed. YYYY-MM-DD
            Example: 2016-07-22.
        line_items (list[ApiV1ArLineItemData]):  The line items for the invoice
        use_real_account_number (bool):  Whether or not the invoice payment instructions will show the real account and
            routing number for the destination account or use virtual account numbers instead. Virtual accounts are safer
            and are preferred in most cases.
        currency_code (None | str | Unset):  ISO 4217 currency code for the invoice. Defaults to USD if not provided.
        internal_note (None | str | Unset):  Internal note for the invoice, visible by users in the organization but not
            visible to payers.
        invoice_number (None | str | Unset):  The payer facing invoice number/identifier.
        payer_memo (None | str | Unset):  Memo for the payer of the invoice.
        po_number (None | str | Unset):  Purchase order number for the invoice, if applicable.
        send_email_option (ApiSendEmailOption | None | Unset):  Rules for emailing the new invoice to payers. Can be
            "DontSend" to skip sending or "SendNow" to send immediately. If omitted, defaults to sending immediately.
        service_period_end_date (datetime.date | None | Unset):  The end date for the service period this invoice
            covers, if applicable. YYYY-MM-DD Example: 2016-07-22.
        service_period_start_date (datetime.date | None | Unset):  The start date for the service period this invoice
            covers, if applicable. YYYY-MM-DD Example: 2016-07-22.
    """

    ach_debit_enabled: bool
    cc_emails: list[str]
    credit_card_enabled: bool
    customer_id: UUID
    destination_account_id: UUID
    due_date: datetime.date
    invoice_date: datetime.date
    line_items: list[ApiV1ArLineItemData]
    use_real_account_number: bool
    currency_code: None | str | Unset = UNSET
    internal_note: None | str | Unset = UNSET
    invoice_number: None | str | Unset = UNSET
    payer_memo: None | str | Unset = UNSET
    po_number: None | str | Unset = UNSET
    send_email_option: ApiSendEmailOption | None | Unset = UNSET
    service_period_end_date: datetime.date | None | Unset = UNSET
    service_period_start_date: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ach_debit_enabled = self.ach_debit_enabled

        cc_emails = self.cc_emails

        credit_card_enabled = self.credit_card_enabled

        customer_id = str(self.customer_id)

        destination_account_id = str(self.destination_account_id)

        due_date = self.due_date.isoformat()

        invoice_date = self.invoice_date.isoformat()

        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()
            line_items.append(line_items_item)

        use_real_account_number = self.use_real_account_number

        currency_code: None | str | Unset
        if isinstance(self.currency_code, Unset):
            currency_code = UNSET
        else:
            currency_code = self.currency_code

        internal_note: None | str | Unset
        if isinstance(self.internal_note, Unset):
            internal_note = UNSET
        else:
            internal_note = self.internal_note

        invoice_number: None | str | Unset
        if isinstance(self.invoice_number, Unset):
            invoice_number = UNSET
        else:
            invoice_number = self.invoice_number

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

        send_email_option: None | str | Unset
        if isinstance(self.send_email_option, Unset):
            send_email_option = UNSET
        elif isinstance(self.send_email_option, ApiSendEmailOption):
            send_email_option = self.send_email_option.value
        else:
            send_email_option = self.send_email_option

        service_period_end_date: None | str | Unset
        if isinstance(self.service_period_end_date, Unset):
            service_period_end_date = UNSET
        elif isinstance(self.service_period_end_date, datetime.date):
            service_period_end_date = self.service_period_end_date.isoformat()
        else:
            service_period_end_date = self.service_period_end_date

        service_period_start_date: None | str | Unset
        if isinstance(self.service_period_start_date, Unset):
            service_period_start_date = UNSET
        elif isinstance(self.service_period_start_date, datetime.date):
            service_period_start_date = self.service_period_start_date.isoformat()
        else:
            service_period_start_date = self.service_period_start_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "achDebitEnabled": ach_debit_enabled,
                "ccEmails": cc_emails,
                "creditCardEnabled": credit_card_enabled,
                "customerId": customer_id,
                "destinationAccountId": destination_account_id,
                "dueDate": due_date,
                "invoiceDate": invoice_date,
                "lineItems": line_items,
                "useRealAccountNumber": use_real_account_number,
            }
        )
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if internal_note is not UNSET:
            field_dict["internalNote"] = internal_note
        if invoice_number is not UNSET:
            field_dict["invoiceNumber"] = invoice_number
        if payer_memo is not UNSET:
            field_dict["payerMemo"] = payer_memo
        if po_number is not UNSET:
            field_dict["poNumber"] = po_number
        if send_email_option is not UNSET:
            field_dict["sendEmailOption"] = send_email_option
        if service_period_end_date is not UNSET:
            field_dict["servicePeriodEndDate"] = service_period_end_date
        if service_period_start_date is not UNSET:
            field_dict["servicePeriodStartDate"] = service_period_start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_ar_line_item_data import ApiV1ArLineItemData

        d = dict(src_dict)
        ach_debit_enabled = d.pop("achDebitEnabled")

        cc_emails = cast(list[str], d.pop("ccEmails"))

        credit_card_enabled = d.pop("creditCardEnabled")

        customer_id = UUID(d.pop("customerId"))

        destination_account_id = UUID(d.pop("destinationAccountId"))

        due_date = datetime.date.fromisoformat(d.pop("dueDate"))

        invoice_date = datetime.date.fromisoformat(d.pop("invoiceDate"))

        line_items = []
        _line_items = d.pop("lineItems")
        for line_items_item_data in _line_items:
            line_items_item = ApiV1ArLineItemData.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        use_real_account_number = d.pop("useRealAccountNumber")

        def _parse_currency_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_code = _parse_currency_code(d.pop("currencyCode", UNSET))

        def _parse_internal_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_note = _parse_internal_note(d.pop("internalNote", UNSET))

        def _parse_invoice_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invoice_number = _parse_invoice_number(d.pop("invoiceNumber", UNSET))

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

        def _parse_send_email_option(data: object) -> ApiSendEmailOption | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                send_email_option_type_0 = ApiSendEmailOption(data)

                return send_email_option_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiSendEmailOption | None | Unset, data)

        send_email_option = _parse_send_email_option(d.pop("sendEmailOption", UNSET))

        def _parse_service_period_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_period_end_date_type_0 = datetime.date.fromisoformat(data)

                return service_period_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        service_period_end_date = _parse_service_period_end_date(d.pop("servicePeriodEndDate", UNSET))

        def _parse_service_period_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_period_start_date_type_0 = datetime.date.fromisoformat(data)

                return service_period_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        service_period_start_date = _parse_service_period_start_date(d.pop("servicePeriodStartDate", UNSET))

        api_v1_ar_invoice_create_request = cls(
            ach_debit_enabled=ach_debit_enabled,
            cc_emails=cc_emails,
            credit_card_enabled=credit_card_enabled,
            customer_id=customer_id,
            destination_account_id=destination_account_id,
            due_date=due_date,
            invoice_date=invoice_date,
            line_items=line_items,
            use_real_account_number=use_real_account_number,
            currency_code=currency_code,
            internal_note=internal_note,
            invoice_number=invoice_number,
            payer_memo=payer_memo,
            po_number=po_number,
            send_email_option=send_email_option,
            service_period_end_date=service_period_end_date,
            service_period_start_date=service_period_start_date,
        )

        api_v1_ar_invoice_create_request.additional_properties = d
        return api_v1_ar_invoice_create_request

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
