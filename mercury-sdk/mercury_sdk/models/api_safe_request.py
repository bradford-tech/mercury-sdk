from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.us_state import USState
from ..models.valuation_type import ValuationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_safe_request_investor import APISafeRequestInvestor
    from ..models.api_safe_request_organization import APISafeRequestOrganization


T = TypeVar("T", bound="APISafeRequest")


@_attrs_define
class APISafeRequest:
    """A summary of a SAFE request.

    Attributes:
        document_url (str):
        expires_at (datetime.datetime):  Example: 2016-07-22T00:00:00Z.
        id (UUID): ID for the SAFE request
        includes_most_favored_nation_clause (bool):
        includes_pro_rata_rights_letter (bool):
        investment_amount (float): A positive dollar amount with at least 1 cent.
        investment_date (datetime.date):  Example: 2016-07-22.
        investor (APISafeRequestInvestor):  Details about the investor buying the equity.
        organization (APISafeRequestOrganization):  Details about the organization selling the equity
        valuation_type (ValuationType):
        canceled_at (datetime.datetime | None | Unset):  Example: 2016-07-22T00:00:00Z.
        discount_rate (float | None | Unset):
        governing_state (None | Unset | USState):
        paid_at (datetime.datetime | None | Unset):  Example: 2016-07-22T00:00:00Z.
        signed_by_investor_at (datetime.datetime | None | Unset):  Example: 2016-07-22T00:00:00Z.
        signed_by_owner_at (datetime.datetime | None | Unset):  Example: 2016-07-22T00:00:00Z.
        valuation_cap (float | None | Unset): A positive dollar amount with at least 1 cent.
    """

    document_url: str
    expires_at: datetime.datetime
    id: UUID
    includes_most_favored_nation_clause: bool
    includes_pro_rata_rights_letter: bool
    investment_amount: float
    investment_date: datetime.date
    investor: APISafeRequestInvestor
    organization: APISafeRequestOrganization
    valuation_type: ValuationType
    canceled_at: datetime.datetime | None | Unset = UNSET
    discount_rate: float | None | Unset = UNSET
    governing_state: None | Unset | USState = UNSET
    paid_at: datetime.datetime | None | Unset = UNSET
    signed_by_investor_at: datetime.datetime | None | Unset = UNSET
    signed_by_owner_at: datetime.datetime | None | Unset = UNSET
    valuation_cap: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_url = self.document_url

        expires_at = self.expires_at.isoformat()

        id = str(self.id)

        includes_most_favored_nation_clause = self.includes_most_favored_nation_clause

        includes_pro_rata_rights_letter = self.includes_pro_rata_rights_letter

        investment_amount = self.investment_amount

        investment_date = self.investment_date.isoformat()

        investor = self.investor.to_dict()

        organization = self.organization.to_dict()

        valuation_type = self.valuation_type.value

        canceled_at: None | str | Unset
        if isinstance(self.canceled_at, Unset):
            canceled_at = UNSET
        elif isinstance(self.canceled_at, datetime.datetime):
            canceled_at = self.canceled_at.isoformat()
        else:
            canceled_at = self.canceled_at

        discount_rate: float | None | Unset
        if isinstance(self.discount_rate, Unset):
            discount_rate = UNSET
        else:
            discount_rate = self.discount_rate

        governing_state: None | str | Unset
        if isinstance(self.governing_state, Unset):
            governing_state = UNSET
        elif isinstance(self.governing_state, USState):
            governing_state = self.governing_state.value
        else:
            governing_state = self.governing_state

        paid_at: None | str | Unset
        if isinstance(self.paid_at, Unset):
            paid_at = UNSET
        elif isinstance(self.paid_at, datetime.datetime):
            paid_at = self.paid_at.isoformat()
        else:
            paid_at = self.paid_at

        signed_by_investor_at: None | str | Unset
        if isinstance(self.signed_by_investor_at, Unset):
            signed_by_investor_at = UNSET
        elif isinstance(self.signed_by_investor_at, datetime.datetime):
            signed_by_investor_at = self.signed_by_investor_at.isoformat()
        else:
            signed_by_investor_at = self.signed_by_investor_at

        signed_by_owner_at: None | str | Unset
        if isinstance(self.signed_by_owner_at, Unset):
            signed_by_owner_at = UNSET
        elif isinstance(self.signed_by_owner_at, datetime.datetime):
            signed_by_owner_at = self.signed_by_owner_at.isoformat()
        else:
            signed_by_owner_at = self.signed_by_owner_at

        valuation_cap: float | None | Unset
        if isinstance(self.valuation_cap, Unset):
            valuation_cap = UNSET
        else:
            valuation_cap = self.valuation_cap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentUrl": document_url,
                "expiresAt": expires_at,
                "id": id,
                "includesMostFavoredNationClause": includes_most_favored_nation_clause,
                "includesProRataRightsLetter": includes_pro_rata_rights_letter,
                "investmentAmount": investment_amount,
                "investmentDate": investment_date,
                "investor": investor,
                "organization": organization,
                "valuationType": valuation_type,
            }
        )
        if canceled_at is not UNSET:
            field_dict["canceledAt"] = canceled_at
        if discount_rate is not UNSET:
            field_dict["discountRate"] = discount_rate
        if governing_state is not UNSET:
            field_dict["governingState"] = governing_state
        if paid_at is not UNSET:
            field_dict["paidAt"] = paid_at
        if signed_by_investor_at is not UNSET:
            field_dict["signedByInvestorAt"] = signed_by_investor_at
        if signed_by_owner_at is not UNSET:
            field_dict["signedByOwnerAt"] = signed_by_owner_at
        if valuation_cap is not UNSET:
            field_dict["valuationCap"] = valuation_cap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_safe_request_investor import APISafeRequestInvestor
        from ..models.api_safe_request_organization import APISafeRequestOrganization

        d = dict(src_dict)
        document_url = d.pop("documentUrl")

        expires_at = datetime.datetime.fromisoformat(d.pop("expiresAt"))

        id = UUID(d.pop("id"))

        includes_most_favored_nation_clause = d.pop("includesMostFavoredNationClause")

        includes_pro_rata_rights_letter = d.pop("includesProRataRightsLetter")

        investment_amount = d.pop("investmentAmount")

        investment_date = datetime.date.fromisoformat(d.pop("investmentDate"))

        investor = APISafeRequestInvestor.from_dict(d.pop("investor"))

        organization = APISafeRequestOrganization.from_dict(d.pop("organization"))

        valuation_type = ValuationType(d.pop("valuationType"))

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

        def _parse_discount_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        discount_rate = _parse_discount_rate(d.pop("discountRate", UNSET))

        def _parse_governing_state(data: object) -> None | Unset | USState:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                governing_state_type_0 = USState(data)

                return governing_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | USState, data)

        governing_state = _parse_governing_state(d.pop("governingState", UNSET))

        def _parse_paid_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paid_at_type_0 = datetime.datetime.fromisoformat(data)

                return paid_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        paid_at = _parse_paid_at(d.pop("paidAt", UNSET))

        def _parse_signed_by_investor_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signed_by_investor_at_type_0 = datetime.datetime.fromisoformat(data)

                return signed_by_investor_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        signed_by_investor_at = _parse_signed_by_investor_at(d.pop("signedByInvestorAt", UNSET))

        def _parse_signed_by_owner_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signed_by_owner_at_type_0 = datetime.datetime.fromisoformat(data)

                return signed_by_owner_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        signed_by_owner_at = _parse_signed_by_owner_at(d.pop("signedByOwnerAt", UNSET))

        def _parse_valuation_cap(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        valuation_cap = _parse_valuation_cap(d.pop("valuationCap", UNSET))

        api_safe_request = cls(
            document_url=document_url,
            expires_at=expires_at,
            id=id,
            includes_most_favored_nation_clause=includes_most_favored_nation_clause,
            includes_pro_rata_rights_letter=includes_pro_rata_rights_letter,
            investment_amount=investment_amount,
            investment_date=investment_date,
            investor=investor,
            organization=organization,
            valuation_type=valuation_type,
            canceled_at=canceled_at,
            discount_rate=discount_rate,
            governing_state=governing_state,
            paid_at=paid_at,
            signed_by_investor_at=signed_by_investor_at,
            signed_by_owner_at=signed_by_owner_at,
            valuation_cap=valuation_cap,
        )

        api_safe_request.additional_properties = d
        return api_safe_request

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
