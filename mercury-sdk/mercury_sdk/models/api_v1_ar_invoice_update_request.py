from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_v1_ar_line_item_data import ApiV1ArLineItemData


T = TypeVar("T", bound="ApiV1ArInvoiceUpdateRequest")


@_attrs_define
class ApiV1ArInvoiceUpdateRequest:
    """The request body to update an invoice.

    Attributes:
        ach_debit_enabled (bool):  Whether or not the invoice can be paid via ACH debit.
        cc_emails (list[str]):  List of emails to be CCed on notifications/reminders.
        credit_card_enabled (bool):  Whether or not the invoice can be paid via credit card. Requires Stripe to be setup
            for the Mercury account.
        due_date (datetime.date):  The date the invoice should be paid by. YYYY-MM-DD Example: 2016-07-22.
        invoice_date (datetime.date):  The date of the invoice, set by the invoice creator. Does not have to be the day
            the invoice was created. It can be business specific i.e. service/sale date. YYYY-MM-DD Example: 2016-07-22.
        invoice_number (str):  The invoice number.
        line_items (list[ApiV1ArLineItemData]):  The line items for the invoice
        use_real_account_number (bool):  Whether or not the invoice payment instructions will show the real account and
            routing number for the destination account or use virtual account numbers instead.
        internal_note (None | str | Unset):  Internal note for the invoice, visible by users in the organization but not
            visible to payers.
        payer_memo (None | str | Unset):  Memo for the payer of the invoice.
        po_number (None | str | Unset):  The purchase order number for the invoice if applicable.
        service_period_end_date (datetime.date | None | Unset):  The end date for the service period this invoice
            covers, if applicable. YYYY-MM-DD Example: 2016-07-22.
        service_period_start_date (datetime.date | None | Unset):  The start date for the service period this invoice
            covers, if applicable. YYYY-MM-DD Example: 2016-07-22.
    """

    ach_debit_enabled: bool
    cc_emails: list[str]
    credit_card_enabled: bool
    due_date: datetime.date
    invoice_date: datetime.date
    invoice_number: str
    line_items: list[ApiV1ArLineItemData]
    use_real_account_number: bool
    internal_note: None | str | Unset = UNSET
    payer_memo: None | str | Unset = UNSET
    po_number: None | str | Unset = UNSET
    service_period_end_date: datetime.date | None | Unset = UNSET
    service_period_start_date: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ach_debit_enabled = self.ach_debit_enabled

        cc_emails = self.cc_emails

        credit_card_enabled = self.credit_card_enabled

        due_date = self.due_date.isoformat()

        invoice_date = self.invoice_date.isoformat()

        invoice_number = self.invoice_number

        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()
            line_items.append(line_items_item)

        use_real_account_number = self.use_real_account_number

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
                "dueDate": due_date,
                "invoiceDate": invoice_date,
                "invoiceNumber": invoice_number,
                "lineItems": line_items,
                "useRealAccountNumber": use_real_account_number,
            }
        )
        if internal_note is not UNSET:
            field_dict["internalNote"] = internal_note
        if payer_memo is not UNSET:
            field_dict["payerMemo"] = payer_memo
        if po_number is not UNSET:
            field_dict["poNumber"] = po_number
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

        due_date = datetime.date.fromisoformat(d.pop("dueDate"))

        invoice_date = datetime.date.fromisoformat(d.pop("invoiceDate"))

        invoice_number = d.pop("invoiceNumber")

        line_items = []
        _line_items = d.pop("lineItems")
        for line_items_item_data in _line_items:
            line_items_item = ApiV1ArLineItemData.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        use_real_account_number = d.pop("useRealAccountNumber")

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

        api_v1_ar_invoice_update_request = cls(
            ach_debit_enabled=ach_debit_enabled,
            cc_emails=cc_emails,
            credit_card_enabled=credit_card_enabled,
            due_date=due_date,
            invoice_date=invoice_date,
            invoice_number=invoice_number,
            line_items=line_items,
            use_real_account_number=use_real_account_number,
            internal_note=internal_note,
            payer_memo=payer_memo,
            po_number=po_number,
            service_period_end_date=service_period_end_date,
            service_period_start_date=service_period_start_date,
        )

        api_v1_ar_invoice_update_request.additional_properties = d
        return api_v1_ar_invoice_update_request

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
