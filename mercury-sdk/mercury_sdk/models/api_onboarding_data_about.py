from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="APIOnboardingDataAbout")


@_attrs_define
class APIOnboardingDataAbout:
    """
    Attributes:
        countries_of_operations (list[str] | None | Unset):  The countries where the company operates.
        country_of_operation (None | str | Unset):
        description (None | str | Unset):
        industry (None | str | Unset):
        legal_business_name (None | str | Unset):
        website (None | str | Unset):
    """

    countries_of_operations: list[str] | None | Unset = UNSET
    country_of_operation: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    industry: None | str | Unset = UNSET
    legal_business_name: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        countries_of_operations: list[str] | None | Unset
        if isinstance(self.countries_of_operations, Unset):
            countries_of_operations = UNSET
        elif isinstance(self.countries_of_operations, list):
            countries_of_operations = self.countries_of_operations

        else:
            countries_of_operations = self.countries_of_operations

        country_of_operation: None | str | Unset
        if isinstance(self.country_of_operation, Unset):
            country_of_operation = UNSET
        else:
            country_of_operation = self.country_of_operation

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        industry: None | str | Unset
        if isinstance(self.industry, Unset):
            industry = UNSET
        else:
            industry = self.industry

        legal_business_name: None | str | Unset
        if isinstance(self.legal_business_name, Unset):
            legal_business_name = UNSET
        else:
            legal_business_name = self.legal_business_name

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if countries_of_operations is not UNSET:
            field_dict["countriesOfOperations"] = countries_of_operations
        if country_of_operation is not UNSET:
            field_dict["countryOfOperation"] = country_of_operation
        if description is not UNSET:
            field_dict["description"] = description
        if industry is not UNSET:
            field_dict["industry"] = industry
        if legal_business_name is not UNSET:
            field_dict["legalBusinessName"] = legal_business_name
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_countries_of_operations(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                countries_of_operations_type_0 = cast(list[str], data)

                return countries_of_operations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        countries_of_operations = _parse_countries_of_operations(d.pop("countriesOfOperations", UNSET))

        def _parse_country_of_operation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_of_operation = _parse_country_of_operation(d.pop("countryOfOperation", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_industry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        industry = _parse_industry(d.pop("industry", UNSET))

        def _parse_legal_business_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_business_name = _parse_legal_business_name(d.pop("legalBusinessName", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        api_onboarding_data_about = cls(
            countries_of_operations=countries_of_operations,
            country_of_operation=country_of_operation,
            description=description,
            industry=industry,
            legal_business_name=legal_business_name,
            website=website,
        )

        api_onboarding_data_about.additional_properties = d
        return api_onboarding_data_about

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
