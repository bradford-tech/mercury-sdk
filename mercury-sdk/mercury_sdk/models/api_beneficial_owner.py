from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.beneficial_owner_job_title import BeneficialOwnerJobTitle
from ..models.citizenship_status import CitizenshipStatus
from ..models.identification_type import IdentificationType
from ..models.is_pep import IsPep
from ..types import UNSET, Unset

T = TypeVar("T", bound="APIBeneficialOwner")


@_attrs_define
class APIBeneficialOwner:
    """Beneficial Owner's Information Gathered From The Onboarding API

    Attributes:
        address1 (None | str | Unset):  Address line 1 of Beneficial Owner's address
        address2 (None | str | Unset):  Address line 2 of Beneficial Owner's address
        citizenship_status (CitizenshipStatus | None | Unset):  Beneficial Owner's Citizenship Status
        city (None | str | Unset):  City of Beneficial Owner's address
        country (None | str | Unset):  Country of Beneficial Owner's address
        date_of_birth (datetime.date | None | Unset):  Beneficial Owner's Date of Birth Example: 2016-07-22.
        email (None | str | Unset):  Beneficial Owner's Email Address
        first_name (None | str | Unset):  Beneficial Owner's First Name
        identification_blob (None | str | Unset):  Beneficial Owner's Identification File
        identification_type (IdentificationType | None | Unset):  Beneficial Owner's Identification File Type
        is_pep (IsPep | None | Unset):  Beneficial Owner's pep status
        job_title (BeneficialOwnerJobTitle | None | Unset):  Beneficial Owner's Job Title
        last_name (None | str | Unset):  Beneficial Owner's Last Name
        other_job_title (None | str | Unset):  Beneficial Owner's Alternate Job Title
        percent_ownership (float | None | Unset):  Beneficial Owner's Ownership Percentage
        phone_number (None | str | Unset):  Beneficial Owner's Phone Number
        postal_code (None | str | Unset):  Postal Code of Beneficial Owner's address
        region (None | str | Unset):  Region or State of Beneficial Owner's address
        social_profile_links (list[str] | None | Unset):  Beneficial Owner's Social Profile Websites
        state (None | str | Unset):  State or Region of Beneficial Owner's address (Deprecated)
    """

    address1: None | str | Unset = UNSET
    address2: None | str | Unset = UNSET
    citizenship_status: CitizenshipStatus | None | Unset = UNSET
    city: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    date_of_birth: datetime.date | None | Unset = UNSET
    email: None | str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    identification_blob: None | str | Unset = UNSET
    identification_type: IdentificationType | None | Unset = UNSET
    is_pep: IsPep | None | Unset = UNSET
    job_title: BeneficialOwnerJobTitle | None | Unset = UNSET
    last_name: None | str | Unset = UNSET
    other_job_title: None | str | Unset = UNSET
    percent_ownership: float | None | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    social_profile_links: list[str] | None | Unset = UNSET
    state: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address1: None | str | Unset
        if isinstance(self.address1, Unset):
            address1 = UNSET
        else:
            address1 = self.address1

        address2: None | str | Unset
        if isinstance(self.address2, Unset):
            address2 = UNSET
        else:
            address2 = self.address2

        citizenship_status: None | str | Unset
        if isinstance(self.citizenship_status, Unset):
            citizenship_status = UNSET
        elif isinstance(self.citizenship_status, CitizenshipStatus):
            citizenship_status = self.citizenship_status.value
        else:
            citizenship_status = self.citizenship_status

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        date_of_birth: None | str | Unset
        if isinstance(self.date_of_birth, Unset):
            date_of_birth = UNSET
        elif isinstance(self.date_of_birth, datetime.date):
            date_of_birth = self.date_of_birth.isoformat()
        else:
            date_of_birth = self.date_of_birth

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        identification_blob: None | str | Unset
        if isinstance(self.identification_blob, Unset):
            identification_blob = UNSET
        else:
            identification_blob = self.identification_blob

        identification_type: None | str | Unset
        if isinstance(self.identification_type, Unset):
            identification_type = UNSET
        elif isinstance(self.identification_type, IdentificationType):
            identification_type = self.identification_type.value
        else:
            identification_type = self.identification_type

        is_pep: None | str | Unset
        if isinstance(self.is_pep, Unset):
            is_pep = UNSET
        elif isinstance(self.is_pep, IsPep):
            is_pep = self.is_pep.value
        else:
            is_pep = self.is_pep

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        elif isinstance(self.job_title, BeneficialOwnerJobTitle):
            job_title = self.job_title.value
        else:
            job_title = self.job_title

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        other_job_title: None | str | Unset
        if isinstance(self.other_job_title, Unset):
            other_job_title = UNSET
        else:
            other_job_title = self.other_job_title

        percent_ownership: float | None | Unset
        if isinstance(self.percent_ownership, Unset):
            percent_ownership = UNSET
        else:
            percent_ownership = self.percent_ownership

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        postal_code: None | str | Unset
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        social_profile_links: list[str] | None | Unset
        if isinstance(self.social_profile_links, Unset):
            social_profile_links = UNSET
        elif isinstance(self.social_profile_links, list):
            social_profile_links = self.social_profile_links

        else:
            social_profile_links = self.social_profile_links

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address1 is not UNSET:
            field_dict["address1"] = address1
        if address2 is not UNSET:
            field_dict["address2"] = address2
        if citizenship_status is not UNSET:
            field_dict["citizenshipStatus"] = citizenship_status
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if identification_blob is not UNSET:
            field_dict["identificationBlob"] = identification_blob
        if identification_type is not UNSET:
            field_dict["identificationType"] = identification_type
        if is_pep is not UNSET:
            field_dict["isPep"] = is_pep
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if other_job_title is not UNSET:
            field_dict["otherJobTitle"] = other_job_title
        if percent_ownership is not UNSET:
            field_dict["percentOwnership"] = percent_ownership
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if region is not UNSET:
            field_dict["region"] = region
        if social_profile_links is not UNSET:
            field_dict["socialProfileLinks"] = social_profile_links
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_address1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address1 = _parse_address1(d.pop("address1", UNSET))

        def _parse_address2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address2 = _parse_address2(d.pop("address2", UNSET))

        def _parse_citizenship_status(data: object) -> CitizenshipStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                citizenship_status_type_0 = CitizenshipStatus(data)

                return citizenship_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CitizenshipStatus | None | Unset, data)

        citizenship_status = _parse_citizenship_status(d.pop("citizenshipStatus", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_date_of_birth(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_birth_type_0 = datetime.date.fromisoformat(data)

                return date_of_birth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date_of_birth = _parse_date_of_birth(d.pop("dateOfBirth", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("firstName", UNSET))

        def _parse_identification_blob(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identification_blob = _parse_identification_blob(d.pop("identificationBlob", UNSET))

        def _parse_identification_type(data: object) -> IdentificationType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                identification_type_type_0 = IdentificationType(data)

                return identification_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IdentificationType | None | Unset, data)

        identification_type = _parse_identification_type(d.pop("identificationType", UNSET))

        def _parse_is_pep(data: object) -> IsPep | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                is_pep_type_0 = IsPep(data)

                return is_pep_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IsPep | None | Unset, data)

        is_pep = _parse_is_pep(d.pop("isPep", UNSET))

        def _parse_job_title(data: object) -> BeneficialOwnerJobTitle | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_title_type_0 = BeneficialOwnerJobTitle(data)

                return job_title_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BeneficialOwnerJobTitle | None | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))

        def _parse_other_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_job_title = _parse_other_job_title(d.pop("otherJobTitle", UNSET))

        def _parse_percent_ownership(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        percent_ownership = _parse_percent_ownership(d.pop("percentOwnership", UNSET))

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

        def _parse_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code = _parse_postal_code(d.pop("postalCode", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_social_profile_links(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                social_profile_links_type_0 = cast(list[str], data)

                return social_profile_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        social_profile_links = _parse_social_profile_links(d.pop("socialProfileLinks", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        api_beneficial_owner = cls(
            address1=address1,
            address2=address2,
            citizenship_status=citizenship_status,
            city=city,
            country=country,
            date_of_birth=date_of_birth,
            email=email,
            first_name=first_name,
            identification_blob=identification_blob,
            identification_type=identification_type,
            is_pep=is_pep,
            job_title=job_title,
            last_name=last_name,
            other_job_title=other_job_title,
            percent_ownership=percent_ownership,
            phone_number=phone_number,
            postal_code=postal_code,
            region=region,
            social_profile_links=social_profile_links,
            state=state,
        )

        api_beneficial_owner.additional_properties = d
        return api_beneficial_owner

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
