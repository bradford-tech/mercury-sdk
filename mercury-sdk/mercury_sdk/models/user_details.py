from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_user_role import ApiUserRole

T = TypeVar("T", bound="UserDetails")


@_attrs_define
class UserDetails:
    """Details of a user within an organization.

    Attributes:
        email (str):  User's email address
        first_name (str):  User's first name
        last_name (str):  User's last name
        organization_role (ApiUserRole):
        user_id (UUID):  Unique identifier for the user
    """

    email: str
    first_name: str
    last_name: str
    organization_role: ApiUserRole
    user_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        organization_role = self.organization_role.value

        user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "organizationRole": organization_role,
                "userId": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        organization_role = ApiUserRole(d.pop("organizationRole"))

        user_id = UUID(d.pop("userId"))

        user_details = cls(
            email=email,
            first_name=first_name,
            last_name=last_name,
            organization_role=organization_role,
            user_id=user_id,
        )

        user_details.additional_properties = d
        return user_details

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
