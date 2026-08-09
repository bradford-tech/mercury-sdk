from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_billing_cadence import ApiBillingCadence
from ..models.api_organization_kind import ApiOrganizationKind
from ..models.api_subscription_tier import ApiSubscriptionTier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_dba import OrganizationDBA


T = TypeVar("T", bound="OrganizationInfo")


@_attrs_define
class OrganizationInfo:
    """Organization information

    Attributes:
        billing_cadence (ApiBillingCadence):
        dbas (list[OrganizationDBA]):  List of DBAs (Doing Business As names) for this organization
        id (UUID):  Unique identifier for the organization Example: 00000000-0000-0000-0000-000000000000.
        kind (ApiOrganizationKind):
        legal_business_name (str):  Legal business name as registered
        subscription_tier (ApiSubscriptionTier):
        ein (None | str | Unset):  Employer Identification Number (EIN), if available
    """

    billing_cadence: ApiBillingCadence
    dbas: list[OrganizationDBA]
    id: UUID
    kind: ApiOrganizationKind
    legal_business_name: str
    subscription_tier: ApiSubscriptionTier
    ein: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_cadence = self.billing_cadence.value

        dbas = []
        for dbas_item_data in self.dbas:
            dbas_item = dbas_item_data.to_dict()
            dbas.append(dbas_item)

        id = str(self.id)

        kind = self.kind.value

        legal_business_name = self.legal_business_name

        subscription_tier = self.subscription_tier.value

        ein: None | str | Unset
        if isinstance(self.ein, Unset):
            ein = UNSET
        else:
            ein = self.ein

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billingCadence": billing_cadence,
                "dbas": dbas,
                "id": id,
                "kind": kind,
                "legalBusinessName": legal_business_name,
                "subscriptionTier": subscription_tier,
            }
        )
        if ein is not UNSET:
            field_dict["ein"] = ein

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_dba import OrganizationDBA

        d = dict(src_dict)
        billing_cadence = ApiBillingCadence(d.pop("billingCadence"))

        dbas = []
        _dbas = d.pop("dbas")
        for dbas_item_data in _dbas:
            dbas_item = OrganizationDBA.from_dict(dbas_item_data)

            dbas.append(dbas_item)

        id = UUID(d.pop("id"))

        kind = ApiOrganizationKind(d.pop("kind"))

        legal_business_name = d.pop("legalBusinessName")

        subscription_tier = ApiSubscriptionTier(d.pop("subscriptionTier"))

        def _parse_ein(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ein = _parse_ein(d.pop("ein", UNSET))

        organization_info = cls(
            billing_cadence=billing_cadence,
            dbas=dbas,
            id=id,
            kind=kind,
            legal_business_name=legal_business_name,
            subscription_tier=subscription_tier,
            ein=ein,
        )

        organization_info.additional_properties = d
        return organization_info

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
