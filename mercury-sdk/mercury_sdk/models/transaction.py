from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mercury_category import MercuryCategory
from ..models.transaction_kind import TransactionKind
from ..models.transaction_status import TransactionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_data import CategoryData
    from ..models.currency_exchange_info import CurrencyExchangeInfo
    from ..models.gl_allocation import GlAllocation
    from ..models.merchant_data import MerchantData
    from ..models.related_transaction_data import RelatedTransactionData
    from ..models.transaction_attachment import TransactionAttachment
    from ..models.transaction_method_data import TransactionMethodData


T = TypeVar("T", bound="Transaction")


@_attrs_define
class Transaction:
    """
    Attributes:
        account_id (UUID):  The external-facing account identifier for the Mercury account that owns this transaction
        amount (float):
        attachments (list[TransactionAttachment]):
        compliant_with_receipt_policy (bool):
        counterparty_id (UUID): ID for a Mercury account.
        counterparty_name (str):
        created_at (datetime.datetime):  Example: 2016-07-22T00:00:00Z.
        dashboard_link (str):
        estimated_delivery_date (datetime.datetime):  Example: 2016-07-22T00:00:00Z.
        gl_allocations (list[GlAllocation]):  GL code allocations assigned to this transaction via a connected
            accounting software
             integration (e.g. QuickBooks, Xero, NetSuite). Each allocation has a GL code name and
             the amount allocated to it; amounts sum to the transaction total when the transaction is
             fully categorized. Empty if no GL codes have been assigned. Distinct from Mercury custom
             categories (see transactionCategoryData).
        has_generated_receipt (bool):
        id (UUID): ID for this transaction
        kind (TransactionKind):
        related_transactions (list[RelatedTransactionData]):
        status (TransactionStatus):
        bank_description (None | str | Unset):
        card_id (None | Unset | UUID):  Id of the card behind this transaction, present on card payments and refunds
            (debit or
             credit); null otherwise, including for card-related fee transactions. Fetch the card's details
             (kind, cardholder, last four, etc.) via the Cards API (`GET /cards/{cardId}`). Supersedes the
             kind-specific `details.creditCardInfo.id` / `details.debitCardInfo.id`.
        category_data (CategoryData | None | Unset):
        check_number (None | str | Unset):  Present for check deposits and mailed checks; Nothing otherwise.
        counterparty_nickname (None | str | Unset):
        credit_account_period_id (None | Unset | UUID): ID for the credit statement period
        currency_exchange_info (CurrencyExchangeInfo | None | Unset):
        details (None | TransactionMethodData | Unset):
        external_memo (None | str | Unset):
        failed_at (datetime.datetime | None | Unset):  Example: 2016-07-22T00:00:00Z.
        fee_id (None | Unset | UUID): ID for this transaction
        general_ledger_code_name (None | str | Unset):  Deprecated: use transactionGlAllocations instead. This field
            does not reflect GL codes
             assigned via Mercury auto-categorization rules. Preserved for backwards compatibility.
        merchant (MerchantData | None | Unset):  Merchant information for card transactions, including the merchant
            category code (MCC),
             merchant ID, Mercury category, and for international transactions, the amount and currency
             in the merchant's local currency. Nothing for non-card transactions.
        mercury_category (MercuryCategory | None | Unset):
        note (None | str | Unset):
        posted_at (datetime.datetime | None | Unset):  Example: 2016-07-22T00:00:00Z.
        reason_for_failure (None | str | Unset):
        request_id (None | str | Unset):
        tracking_number (None | str | Unset):  Present for transactions that have tracking numbers (e.g., RTP, ACH,
            wires); Nothing otherwise.
    """

    account_id: UUID
    amount: float
    attachments: list[TransactionAttachment]
    compliant_with_receipt_policy: bool
    counterparty_id: UUID
    counterparty_name: str
    created_at: datetime.datetime
    dashboard_link: str
    estimated_delivery_date: datetime.datetime
    gl_allocations: list[GlAllocation]
    has_generated_receipt: bool
    id: UUID
    kind: TransactionKind
    related_transactions: list[RelatedTransactionData]
    status: TransactionStatus
    bank_description: None | str | Unset = UNSET
    card_id: None | Unset | UUID = UNSET
    category_data: CategoryData | None | Unset = UNSET
    check_number: None | str | Unset = UNSET
    counterparty_nickname: None | str | Unset = UNSET
    credit_account_period_id: None | Unset | UUID = UNSET
    currency_exchange_info: CurrencyExchangeInfo | None | Unset = UNSET
    details: None | TransactionMethodData | Unset = UNSET
    external_memo: None | str | Unset = UNSET
    failed_at: datetime.datetime | None | Unset = UNSET
    fee_id: None | Unset | UUID = UNSET
    general_ledger_code_name: None | str | Unset = UNSET
    merchant: MerchantData | None | Unset = UNSET
    mercury_category: MercuryCategory | None | Unset = UNSET
    note: None | str | Unset = UNSET
    posted_at: datetime.datetime | None | Unset = UNSET
    reason_for_failure: None | str | Unset = UNSET
    request_id: None | str | Unset = UNSET
    tracking_number: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.category_data import CategoryData
        from ..models.currency_exchange_info import CurrencyExchangeInfo
        from ..models.merchant_data import MerchantData
        from ..models.transaction_method_data import TransactionMethodData

        account_id = str(self.account_id)

        amount = self.amount

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()
            attachments.append(attachments_item)

        compliant_with_receipt_policy = self.compliant_with_receipt_policy

        counterparty_id = str(self.counterparty_id)

        counterparty_name = self.counterparty_name

        created_at = self.created_at.isoformat()

        dashboard_link = self.dashboard_link

        estimated_delivery_date = self.estimated_delivery_date.isoformat()

        gl_allocations = []
        for gl_allocations_item_data in self.gl_allocations:
            gl_allocations_item = gl_allocations_item_data.to_dict()
            gl_allocations.append(gl_allocations_item)

        has_generated_receipt = self.has_generated_receipt

        id = str(self.id)

        kind = self.kind.value

        related_transactions = []
        for related_transactions_item_data in self.related_transactions:
            related_transactions_item = related_transactions_item_data.to_dict()
            related_transactions.append(related_transactions_item)

        status = self.status.value

        bank_description: None | str | Unset
        if isinstance(self.bank_description, Unset):
            bank_description = UNSET
        else:
            bank_description = self.bank_description

        card_id: None | str | Unset
        if isinstance(self.card_id, Unset):
            card_id = UNSET
        elif isinstance(self.card_id, UUID):
            card_id = str(self.card_id)
        else:
            card_id = self.card_id

        category_data: dict[str, Any] | None | Unset
        if isinstance(self.category_data, Unset):
            category_data = UNSET
        elif isinstance(self.category_data, CategoryData):
            category_data = self.category_data.to_dict()
        else:
            category_data = self.category_data

        check_number: None | str | Unset
        if isinstance(self.check_number, Unset):
            check_number = UNSET
        else:
            check_number = self.check_number

        counterparty_nickname: None | str | Unset
        if isinstance(self.counterparty_nickname, Unset):
            counterparty_nickname = UNSET
        else:
            counterparty_nickname = self.counterparty_nickname

        credit_account_period_id: None | str | Unset
        if isinstance(self.credit_account_period_id, Unset):
            credit_account_period_id = UNSET
        elif isinstance(self.credit_account_period_id, UUID):
            credit_account_period_id = str(self.credit_account_period_id)
        else:
            credit_account_period_id = self.credit_account_period_id

        currency_exchange_info: dict[str, Any] | None | Unset
        if isinstance(self.currency_exchange_info, Unset):
            currency_exchange_info = UNSET
        elif isinstance(self.currency_exchange_info, CurrencyExchangeInfo):
            currency_exchange_info = self.currency_exchange_info.to_dict()
        else:
            currency_exchange_info = self.currency_exchange_info

        details: dict[str, Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, TransactionMethodData):
            details = self.details.to_dict()
        else:
            details = self.details

        external_memo: None | str | Unset
        if isinstance(self.external_memo, Unset):
            external_memo = UNSET
        else:
            external_memo = self.external_memo

        failed_at: None | str | Unset
        if isinstance(self.failed_at, Unset):
            failed_at = UNSET
        elif isinstance(self.failed_at, datetime.datetime):
            failed_at = self.failed_at.isoformat()
        else:
            failed_at = self.failed_at

        fee_id: None | str | Unset
        if isinstance(self.fee_id, Unset):
            fee_id = UNSET
        elif isinstance(self.fee_id, UUID):
            fee_id = str(self.fee_id)
        else:
            fee_id = self.fee_id

        general_ledger_code_name: None | str | Unset
        if isinstance(self.general_ledger_code_name, Unset):
            general_ledger_code_name = UNSET
        else:
            general_ledger_code_name = self.general_ledger_code_name

        merchant: dict[str, Any] | None | Unset
        if isinstance(self.merchant, Unset):
            merchant = UNSET
        elif isinstance(self.merchant, MerchantData):
            merchant = self.merchant.to_dict()
        else:
            merchant = self.merchant

        mercury_category: None | str | Unset
        if isinstance(self.mercury_category, Unset):
            mercury_category = UNSET
        elif isinstance(self.mercury_category, MercuryCategory):
            mercury_category = self.mercury_category.value
        else:
            mercury_category = self.mercury_category

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        posted_at: None | str | Unset
        if isinstance(self.posted_at, Unset):
            posted_at = UNSET
        elif isinstance(self.posted_at, datetime.datetime):
            posted_at = self.posted_at.isoformat()
        else:
            posted_at = self.posted_at

        reason_for_failure: None | str | Unset
        if isinstance(self.reason_for_failure, Unset):
            reason_for_failure = UNSET
        else:
            reason_for_failure = self.reason_for_failure

        request_id: None | str | Unset
        if isinstance(self.request_id, Unset):
            request_id = UNSET
        else:
            request_id = self.request_id

        tracking_number: None | str | Unset
        if isinstance(self.tracking_number, Unset):
            tracking_number = UNSET
        else:
            tracking_number = self.tracking_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "amount": amount,
                "attachments": attachments,
                "compliantWithReceiptPolicy": compliant_with_receipt_policy,
                "counterpartyId": counterparty_id,
                "counterpartyName": counterparty_name,
                "createdAt": created_at,
                "dashboardLink": dashboard_link,
                "estimatedDeliveryDate": estimated_delivery_date,
                "glAllocations": gl_allocations,
                "hasGeneratedReceipt": has_generated_receipt,
                "id": id,
                "kind": kind,
                "relatedTransactions": related_transactions,
                "status": status,
            }
        )
        if bank_description is not UNSET:
            field_dict["bankDescription"] = bank_description
        if card_id is not UNSET:
            field_dict["cardId"] = card_id
        if category_data is not UNSET:
            field_dict["categoryData"] = category_data
        if check_number is not UNSET:
            field_dict["checkNumber"] = check_number
        if counterparty_nickname is not UNSET:
            field_dict["counterpartyNickname"] = counterparty_nickname
        if credit_account_period_id is not UNSET:
            field_dict["creditAccountPeriodId"] = credit_account_period_id
        if currency_exchange_info is not UNSET:
            field_dict["currencyExchangeInfo"] = currency_exchange_info
        if details is not UNSET:
            field_dict["details"] = details
        if external_memo is not UNSET:
            field_dict["externalMemo"] = external_memo
        if failed_at is not UNSET:
            field_dict["failedAt"] = failed_at
        if fee_id is not UNSET:
            field_dict["feeId"] = fee_id
        if general_ledger_code_name is not UNSET:
            field_dict["generalLedgerCodeName"] = general_ledger_code_name
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if mercury_category is not UNSET:
            field_dict["mercuryCategory"] = mercury_category
        if note is not UNSET:
            field_dict["note"] = note
        if posted_at is not UNSET:
            field_dict["postedAt"] = posted_at
        if reason_for_failure is not UNSET:
            field_dict["reasonForFailure"] = reason_for_failure
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_data import CategoryData
        from ..models.currency_exchange_info import CurrencyExchangeInfo
        from ..models.gl_allocation import GlAllocation
        from ..models.merchant_data import MerchantData
        from ..models.related_transaction_data import RelatedTransactionData
        from ..models.transaction_attachment import TransactionAttachment
        from ..models.transaction_method_data import TransactionMethodData

        d = dict(src_dict)
        account_id = UUID(d.pop("accountId"))

        amount = d.pop("amount")

        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = TransactionAttachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        compliant_with_receipt_policy = d.pop("compliantWithReceiptPolicy")

        counterparty_id = UUID(d.pop("counterpartyId"))

        counterparty_name = d.pop("counterpartyName")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        dashboard_link = d.pop("dashboardLink")

        estimated_delivery_date = datetime.datetime.fromisoformat(d.pop("estimatedDeliveryDate"))

        gl_allocations = []
        _gl_allocations = d.pop("glAllocations")
        for gl_allocations_item_data in _gl_allocations:
            gl_allocations_item = GlAllocation.from_dict(gl_allocations_item_data)

            gl_allocations.append(gl_allocations_item)

        has_generated_receipt = d.pop("hasGeneratedReceipt")

        id = UUID(d.pop("id"))

        kind = TransactionKind(d.pop("kind"))

        related_transactions = []
        _related_transactions = d.pop("relatedTransactions")
        for related_transactions_item_data in _related_transactions:
            related_transactions_item = RelatedTransactionData.from_dict(related_transactions_item_data)

            related_transactions.append(related_transactions_item)

        status = TransactionStatus(d.pop("status"))

        def _parse_bank_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_description = _parse_bank_description(d.pop("bankDescription", UNSET))

        def _parse_card_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                card_id_type_0 = UUID(data)

                return card_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        card_id = _parse_card_id(d.pop("cardId", UNSET))

        def _parse_category_data(data: object) -> CategoryData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                category_data_type_0 = CategoryData.from_dict(data)

                return category_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CategoryData | None | Unset, data)

        category_data = _parse_category_data(d.pop("categoryData", UNSET))

        def _parse_check_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_number = _parse_check_number(d.pop("checkNumber", UNSET))

        def _parse_counterparty_nickname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        counterparty_nickname = _parse_counterparty_nickname(d.pop("counterpartyNickname", UNSET))

        def _parse_credit_account_period_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credit_account_period_id_type_0 = UUID(data)

                return credit_account_period_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        credit_account_period_id = _parse_credit_account_period_id(d.pop("creditAccountPeriodId", UNSET))

        def _parse_currency_exchange_info(data: object) -> CurrencyExchangeInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                currency_exchange_info_type_0 = CurrencyExchangeInfo.from_dict(data)

                return currency_exchange_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CurrencyExchangeInfo | None | Unset, data)

        currency_exchange_info = _parse_currency_exchange_info(d.pop("currencyExchangeInfo", UNSET))

        def _parse_details(data: object) -> None | TransactionMethodData | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = TransactionMethodData.from_dict(data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionMethodData | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        def _parse_external_memo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_memo = _parse_external_memo(d.pop("externalMemo", UNSET))

        def _parse_failed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                failed_at_type_0 = datetime.datetime.fromisoformat(data)

                return failed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        failed_at = _parse_failed_at(d.pop("failedAt", UNSET))

        def _parse_fee_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fee_id_type_0 = UUID(data)

                return fee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        fee_id = _parse_fee_id(d.pop("feeId", UNSET))

        def _parse_general_ledger_code_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        general_ledger_code_name = _parse_general_ledger_code_name(d.pop("generalLedgerCodeName", UNSET))

        def _parse_merchant(data: object) -> MerchantData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                merchant_type_0 = MerchantData.from_dict(data)

                return merchant_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MerchantData | None | Unset, data)

        merchant = _parse_merchant(d.pop("merchant", UNSET))

        def _parse_mercury_category(data: object) -> MercuryCategory | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mercury_category_type_0 = MercuryCategory(data)

                return mercury_category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MercuryCategory | None | Unset, data)

        mercury_category = _parse_mercury_category(d.pop("mercuryCategory", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_posted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                posted_at_type_0 = datetime.datetime.fromisoformat(data)

                return posted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        posted_at = _parse_posted_at(d.pop("postedAt", UNSET))

        def _parse_reason_for_failure(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason_for_failure = _parse_reason_for_failure(d.pop("reasonForFailure", UNSET))

        def _parse_request_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_id = _parse_request_id(d.pop("requestId", UNSET))

        def _parse_tracking_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tracking_number = _parse_tracking_number(d.pop("trackingNumber", UNSET))

        transaction = cls(
            account_id=account_id,
            amount=amount,
            attachments=attachments,
            compliant_with_receipt_policy=compliant_with_receipt_policy,
            counterparty_id=counterparty_id,
            counterparty_name=counterparty_name,
            created_at=created_at,
            dashboard_link=dashboard_link,
            estimated_delivery_date=estimated_delivery_date,
            gl_allocations=gl_allocations,
            has_generated_receipt=has_generated_receipt,
            id=id,
            kind=kind,
            related_transactions=related_transactions,
            status=status,
            bank_description=bank_description,
            card_id=card_id,
            category_data=category_data,
            check_number=check_number,
            counterparty_nickname=counterparty_nickname,
            credit_account_period_id=credit_account_period_id,
            currency_exchange_info=currency_exchange_info,
            details=details,
            external_memo=external_memo,
            failed_at=failed_at,
            fee_id=fee_id,
            general_ledger_code_name=general_ledger_code_name,
            merchant=merchant,
            mercury_category=mercury_category,
            note=note,
            posted_at=posted_at,
            reason_for_failure=reason_for_failure,
            request_id=request_id,
            tracking_number=tracking_number,
        )

        transaction.additional_properties = d
        return transaction

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
