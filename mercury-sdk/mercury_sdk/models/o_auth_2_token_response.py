from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuth2TokenResponse")


@_attrs_define
class OAuth2TokenResponse:
    """
    Attributes:
        access_token (str): The access token issued by the authorization server.
        token_type (str): The type of the token issued. Value is case insensitive and should be "Bearer".
        expires_in (int | Unset): The lifetime in seconds of the access token. For example, the value "3600" denotes
            that the access token will expire in one hour from the time the response was generated. Default: 0.
        refresh_token (str | Unset): The refresh token, which can be used to obtain new access tokens using the same
            authorization grant.
        scope (str | Unset): The scope of the access token. A space-separated list of scopes.
    """

    access_token: str
    token_type: str
    expires_in: int | Unset = 0
    refresh_token: str | Unset = UNSET
    scope: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        token_type = self.token_type

        expires_in = self.expires_in

        refresh_token = self.refresh_token

        scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_token": access_token,
                "token_type": token_type,
            }
        )
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token")

        token_type = d.pop("token_type")

        expires_in = d.pop("expires_in", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        scope = d.pop("scope", UNSET)

        o_auth_2_token_response = cls(
            access_token=access_token,
            token_type=token_type,
            expires_in=expires_in,
            refresh_token=refresh_token,
            scope=scope,
        )

        o_auth_2_token_response.additional_properties = d
        return o_auth_2_token_response

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
