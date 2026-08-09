from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mercury_category import MercuryCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="MerchantData")


@_attrs_define
class MerchantData:
    """Merchant information for card transactions

    Attributes:
        amount (int | None | Unset):  The transaction amount in the smallest unit of the merchant's currency
             (e.g., cents for USD/EUR, yen for JPY, fils for BHD).
             For debits this is negative, for credits positive.
             Use 'merchantCurrency' to determine the appropriate decimal scaling:
             most currencies use 2 decimal places (divide by 100), but JPY uses 0
             (no division needed) and BHD/KWD/OMR use 3 (divide by 1000).
             This is useful for international transactions where the merchant charges in a
             currency different from the account currency. Nothing if not available.
        category (MercuryCategory | None | Unset):  Mercury category for the merchant (e.g., "Restaurants", "Software")
        category_code (None | str | Unset):  4-digit merchant category code (MCC) for card transactions
        currency (None | str | Unset):  ISO 4217 currency code of the merchant's currency (e.g., "EUR", "GBP", "JPY").
             Nothing if not available.
        id (None | str | Unset):  Merchant ID for card transactions
    """

    amount: int | None | Unset = UNSET
    category: MercuryCategory | None | Unset = UNSET
    category_code: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount: int | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, MercuryCategory):
            category = self.category.value
        else:
            category = self.category

        category_code: None | str | Unset
        if isinstance(self.category_code, Unset):
            category_code = UNSET
        else:
            category_code = self.category_code

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if category is not UNSET:
            field_dict["category"] = category
        if category_code is not UNSET:
            field_dict["categoryCode"] = category_code
        if currency is not UNSET:
            field_dict["currency"] = currency
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_amount(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_category(data: object) -> MercuryCategory | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_0 = MercuryCategory(data)

                return category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MercuryCategory | None | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_category_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_code = _parse_category_code(d.pop("categoryCode", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        merchant_data = cls(
            amount=amount,
            category=category,
            category_code=category_code,
            currency=currency,
            id=id,
        )

        merchant_data.additional_properties = d
        return merchant_data

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
