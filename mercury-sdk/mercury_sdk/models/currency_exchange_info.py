from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrencyExchangeInfo")


@_attrs_define
class CurrencyExchangeInfo:
    """
    Attributes:
        converted_from_amount (float):
        converted_from_currency (str):
        converted_to_amount (float):
        converted_to_currency (str):
        exchange_rate (float):  Exchange rate goes from "from currency" to "to currency"
             (ie from currency * exchange rate = to currency)
        fee_amount (float):
        fee_percentage (float):
        fee_transaction_id (None | Unset | UUID): ID for this transaction
    """

    converted_from_amount: float
    converted_from_currency: str
    converted_to_amount: float
    converted_to_currency: str
    exchange_rate: float
    fee_amount: float
    fee_percentage: float
    fee_transaction_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        converted_from_amount = self.converted_from_amount

        converted_from_currency = self.converted_from_currency

        converted_to_amount = self.converted_to_amount

        converted_to_currency = self.converted_to_currency

        exchange_rate = self.exchange_rate

        fee_amount = self.fee_amount

        fee_percentage = self.fee_percentage

        fee_transaction_id: None | str | Unset
        if isinstance(self.fee_transaction_id, Unset):
            fee_transaction_id = UNSET
        elif isinstance(self.fee_transaction_id, UUID):
            fee_transaction_id = str(self.fee_transaction_id)
        else:
            fee_transaction_id = self.fee_transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "convertedFromAmount": converted_from_amount,
                "convertedFromCurrency": converted_from_currency,
                "convertedToAmount": converted_to_amount,
                "convertedToCurrency": converted_to_currency,
                "exchangeRate": exchange_rate,
                "feeAmount": fee_amount,
                "feePercentage": fee_percentage,
            }
        )
        if fee_transaction_id is not UNSET:
            field_dict["feeTransactionId"] = fee_transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        converted_from_amount = d.pop("convertedFromAmount")

        converted_from_currency = d.pop("convertedFromCurrency")

        converted_to_amount = d.pop("convertedToAmount")

        converted_to_currency = d.pop("convertedToCurrency")

        exchange_rate = d.pop("exchangeRate")

        fee_amount = d.pop("feeAmount")

        fee_percentage = d.pop("feePercentage")

        def _parse_fee_transaction_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fee_transaction_id_type_0 = UUID(data)

                return fee_transaction_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        fee_transaction_id = _parse_fee_transaction_id(d.pop("feeTransactionId", UNSET))

        currency_exchange_info = cls(
            converted_from_amount=converted_from_amount,
            converted_from_currency=converted_from_currency,
            converted_to_amount=converted_to_amount,
            converted_to_currency=converted_to_currency,
            exchange_rate=exchange_rate,
            fee_amount=fee_amount,
            fee_percentage=fee_percentage,
            fee_transaction_id=fee_transaction_id,
        )

        currency_exchange_info.additional_properties = d
        return currency_exchange_info

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
