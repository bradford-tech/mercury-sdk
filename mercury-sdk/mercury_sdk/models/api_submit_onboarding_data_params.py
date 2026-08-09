from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_application_type import APIApplicationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_beneficial_owner import APIBeneficialOwner
    from ..models.api_business_address import APIBusinessAddress
    from ..models.api_business_contact_details import APIBusinessContactDetails
    from ..models.api_formation_details import APIFormationDetails
    from ..models.api_onboarding_data_about import APIOnboardingDataAbout


T = TypeVar("T", bound="APISubmitOnboardingDataParams")


@_attrs_define
class APISubmitOnboardingDataParams:
    """
    Attributes:
        beneficial_owners (list[APIBeneficialOwner]):
        partner (str):
        about (APIOnboardingDataAbout | None | Unset):
        application_type (APIApplicationType | None | Unset):
        business_contact_details (APIBusinessContactDetails | None | Unset):
        business_legal_address (APIBusinessAddress | None | Unset):
        business_physical_address (APIBusinessAddress | None | Unset):
        formation_details (APIFormationDetails | None | Unset):
        invite_email (None | str | Unset):
        webhook_url (None | str | Unset):
    """

    beneficial_owners: list[APIBeneficialOwner]
    partner: str
    about: APIOnboardingDataAbout | None | Unset = UNSET
    application_type: APIApplicationType | None | Unset = UNSET
    business_contact_details: APIBusinessContactDetails | None | Unset = UNSET
    business_legal_address: APIBusinessAddress | None | Unset = UNSET
    business_physical_address: APIBusinessAddress | None | Unset = UNSET
    formation_details: APIFormationDetails | None | Unset = UNSET
    invite_email: None | str | Unset = UNSET
    webhook_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_business_address import APIBusinessAddress
        from ..models.api_business_contact_details import APIBusinessContactDetails
        from ..models.api_formation_details import APIFormationDetails
        from ..models.api_onboarding_data_about import APIOnboardingDataAbout

        beneficial_owners = []
        for beneficial_owners_item_data in self.beneficial_owners:
            beneficial_owners_item = beneficial_owners_item_data.to_dict()
            beneficial_owners.append(beneficial_owners_item)

        partner = self.partner

        about: dict[str, Any] | None | Unset
        if isinstance(self.about, Unset):
            about = UNSET
        elif isinstance(self.about, APIOnboardingDataAbout):
            about = self.about.to_dict()
        else:
            about = self.about

        application_type: None | str | Unset
        if isinstance(self.application_type, Unset):
            application_type = UNSET
        elif isinstance(self.application_type, APIApplicationType):
            application_type = self.application_type.value
        else:
            application_type = self.application_type

        business_contact_details: dict[str, Any] | None | Unset
        if isinstance(self.business_contact_details, Unset):
            business_contact_details = UNSET
        elif isinstance(self.business_contact_details, APIBusinessContactDetails):
            business_contact_details = self.business_contact_details.to_dict()
        else:
            business_contact_details = self.business_contact_details

        business_legal_address: dict[str, Any] | None | Unset
        if isinstance(self.business_legal_address, Unset):
            business_legal_address = UNSET
        elif isinstance(self.business_legal_address, APIBusinessAddress):
            business_legal_address = self.business_legal_address.to_dict()
        else:
            business_legal_address = self.business_legal_address

        business_physical_address: dict[str, Any] | None | Unset
        if isinstance(self.business_physical_address, Unset):
            business_physical_address = UNSET
        elif isinstance(self.business_physical_address, APIBusinessAddress):
            business_physical_address = self.business_physical_address.to_dict()
        else:
            business_physical_address = self.business_physical_address

        formation_details: dict[str, Any] | None | Unset
        if isinstance(self.formation_details, Unset):
            formation_details = UNSET
        elif isinstance(self.formation_details, APIFormationDetails):
            formation_details = self.formation_details.to_dict()
        else:
            formation_details = self.formation_details

        invite_email: None | str | Unset
        if isinstance(self.invite_email, Unset):
            invite_email = UNSET
        else:
            invite_email = self.invite_email

        webhook_url: None | str | Unset
        if isinstance(self.webhook_url, Unset):
            webhook_url = UNSET
        else:
            webhook_url = self.webhook_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "beneficialOwners": beneficial_owners,
                "partner": partner,
            }
        )
        if about is not UNSET:
            field_dict["about"] = about
        if application_type is not UNSET:
            field_dict["applicationType"] = application_type
        if business_contact_details is not UNSET:
            field_dict["businessContactDetails"] = business_contact_details
        if business_legal_address is not UNSET:
            field_dict["businessLegalAddress"] = business_legal_address
        if business_physical_address is not UNSET:
            field_dict["businessPhysicalAddress"] = business_physical_address
        if formation_details is not UNSET:
            field_dict["formationDetails"] = formation_details
        if invite_email is not UNSET:
            field_dict["inviteEmail"] = invite_email
        if webhook_url is not UNSET:
            field_dict["webhookURL"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_beneficial_owner import APIBeneficialOwner
        from ..models.api_business_address import APIBusinessAddress
        from ..models.api_business_contact_details import APIBusinessContactDetails
        from ..models.api_formation_details import APIFormationDetails
        from ..models.api_onboarding_data_about import APIOnboardingDataAbout

        d = dict(src_dict)
        beneficial_owners = []
        _beneficial_owners = d.pop("beneficialOwners")
        for beneficial_owners_item_data in _beneficial_owners:
            beneficial_owners_item = APIBeneficialOwner.from_dict(beneficial_owners_item_data)

            beneficial_owners.append(beneficial_owners_item)

        partner = d.pop("partner")

        def _parse_about(data: object) -> APIOnboardingDataAbout | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                about_type_0 = APIOnboardingDataAbout.from_dict(data)

                return about_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(APIOnboardingDataAbout | None | Unset, data)

        about = _parse_about(d.pop("about", UNSET))

        def _parse_application_type(data: object) -> APIApplicationType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                application_type_type_0 = APIApplicationType(data)

                return application_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(APIApplicationType | None | Unset, data)

        application_type = _parse_application_type(d.pop("applicationType", UNSET))

        def _parse_business_contact_details(data: object) -> APIBusinessContactDetails | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                business_contact_details_type_0 = APIBusinessContactDetails.from_dict(data)

                return business_contact_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(APIBusinessContactDetails | None | Unset, data)

        business_contact_details = _parse_business_contact_details(d.pop("businessContactDetails", UNSET))

        def _parse_business_legal_address(data: object) -> APIBusinessAddress | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                business_legal_address_type_0 = APIBusinessAddress.from_dict(data)

                return business_legal_address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(APIBusinessAddress | None | Unset, data)

        business_legal_address = _parse_business_legal_address(d.pop("businessLegalAddress", UNSET))

        def _parse_business_physical_address(data: object) -> APIBusinessAddress | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                business_physical_address_type_0 = APIBusinessAddress.from_dict(data)

                return business_physical_address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(APIBusinessAddress | None | Unset, data)

        business_physical_address = _parse_business_physical_address(d.pop("businessPhysicalAddress", UNSET))

        def _parse_formation_details(data: object) -> APIFormationDetails | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                formation_details_type_0 = APIFormationDetails.from_dict(data)

                return formation_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(APIFormationDetails | None | Unset, data)

        formation_details = _parse_formation_details(d.pop("formationDetails", UNSET))

        def _parse_invite_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invite_email = _parse_invite_email(d.pop("inviteEmail", UNSET))

        def _parse_webhook_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        webhook_url = _parse_webhook_url(d.pop("webhookURL", UNSET))

        api_submit_onboarding_data_params = cls(
            beneficial_owners=beneficial_owners,
            partner=partner,
            about=about,
            application_type=application_type,
            business_contact_details=business_contact_details,
            business_legal_address=business_legal_address,
            business_physical_address=business_physical_address,
            formation_details=formation_details,
            invite_email=invite_email,
            webhook_url=webhook_url,
        )

        api_submit_onboarding_data_params.additional_properties = d
        return api_submit_onboarding_data_params

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
