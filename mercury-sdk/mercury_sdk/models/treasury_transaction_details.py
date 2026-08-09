from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TreasuryTransactionDetails")


@_attrs_define
class TreasuryTransactionDetails:
    """
    Attributes:
        credit_description (None | str | Unset):
        deposit_counterparty_id (None | Unset | UUID): ID for a Mercury account.
        fee_description (None | str | Unset):
        manual_amendment_description (None | str | Unset):
        security (None | str | Unset):
        sweep_direction (None | str | Unset):
        trade_action (None | str | Unset):
        withdrawal_counterparty_id (None | Unset | UUID): ID for a Mercury account.
    """

    credit_description: None | str | Unset = UNSET
    deposit_counterparty_id: None | Unset | UUID = UNSET
    fee_description: None | str | Unset = UNSET
    manual_amendment_description: None | str | Unset = UNSET
    security: None | str | Unset = UNSET
    sweep_direction: None | str | Unset = UNSET
    trade_action: None | str | Unset = UNSET
    withdrawal_counterparty_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credit_description: None | str | Unset
        if isinstance(self.credit_description, Unset):
            credit_description = UNSET
        else:
            credit_description = self.credit_description

        deposit_counterparty_id: None | str | Unset
        if isinstance(self.deposit_counterparty_id, Unset):
            deposit_counterparty_id = UNSET
        elif isinstance(self.deposit_counterparty_id, UUID):
            deposit_counterparty_id = str(self.deposit_counterparty_id)
        else:
            deposit_counterparty_id = self.deposit_counterparty_id

        fee_description: None | str | Unset
        if isinstance(self.fee_description, Unset):
            fee_description = UNSET
        else:
            fee_description = self.fee_description

        manual_amendment_description: None | str | Unset
        if isinstance(self.manual_amendment_description, Unset):
            manual_amendment_description = UNSET
        else:
            manual_amendment_description = self.manual_amendment_description

        security: None | str | Unset
        if isinstance(self.security, Unset):
            security = UNSET
        else:
            security = self.security

        sweep_direction: None | str | Unset
        if isinstance(self.sweep_direction, Unset):
            sweep_direction = UNSET
        else:
            sweep_direction = self.sweep_direction

        trade_action: None | str | Unset
        if isinstance(self.trade_action, Unset):
            trade_action = UNSET
        else:
            trade_action = self.trade_action

        withdrawal_counterparty_id: None | str | Unset
        if isinstance(self.withdrawal_counterparty_id, Unset):
            withdrawal_counterparty_id = UNSET
        elif isinstance(self.withdrawal_counterparty_id, UUID):
            withdrawal_counterparty_id = str(self.withdrawal_counterparty_id)
        else:
            withdrawal_counterparty_id = self.withdrawal_counterparty_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credit_description is not UNSET:
            field_dict["creditDescription"] = credit_description
        if deposit_counterparty_id is not UNSET:
            field_dict["depositCounterpartyId"] = deposit_counterparty_id
        if fee_description is not UNSET:
            field_dict["feeDescription"] = fee_description
        if manual_amendment_description is not UNSET:
            field_dict["manualAmendmentDescription"] = manual_amendment_description
        if security is not UNSET:
            field_dict["security"] = security
        if sweep_direction is not UNSET:
            field_dict["sweepDirection"] = sweep_direction
        if trade_action is not UNSET:
            field_dict["tradeAction"] = trade_action
        if withdrawal_counterparty_id is not UNSET:
            field_dict["withdrawalCounterpartyId"] = withdrawal_counterparty_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_credit_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        credit_description = _parse_credit_description(d.pop("creditDescription", UNSET))

        def _parse_deposit_counterparty_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deposit_counterparty_id_type_0 = UUID(data)

                return deposit_counterparty_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        deposit_counterparty_id = _parse_deposit_counterparty_id(d.pop("depositCounterpartyId", UNSET))

        def _parse_fee_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fee_description = _parse_fee_description(d.pop("feeDescription", UNSET))

        def _parse_manual_amendment_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        manual_amendment_description = _parse_manual_amendment_description(d.pop("manualAmendmentDescription", UNSET))

        def _parse_security(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        security = _parse_security(d.pop("security", UNSET))

        def _parse_sweep_direction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sweep_direction = _parse_sweep_direction(d.pop("sweepDirection", UNSET))

        def _parse_trade_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_action = _parse_trade_action(d.pop("tradeAction", UNSET))

        def _parse_withdrawal_counterparty_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                withdrawal_counterparty_id_type_0 = UUID(data)

                return withdrawal_counterparty_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        withdrawal_counterparty_id = _parse_withdrawal_counterparty_id(d.pop("withdrawalCounterpartyId", UNSET))

        treasury_transaction_details = cls(
            credit_description=credit_description,
            deposit_counterparty_id=deposit_counterparty_id,
            fee_description=fee_description,
            manual_amendment_description=manual_amendment_description,
            security=security,
            sweep_direction=sweep_direction,
            trade_action=trade_action,
            withdrawal_counterparty_id=withdrawal_counterparty_id,
        )

        treasury_transaction_details.additional_properties = d
        return treasury_transaction_details

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
