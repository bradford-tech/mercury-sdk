from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_2_token_request_grant_type import OAuth2TokenRequestGrantType

T = TypeVar("T", bound="OAuth2TokenRequest")


@_attrs_define
class OAuth2TokenRequest:
    r"""
    Attributes:
        code (str): The authorization code received from the authorization server. Required when grant_type is
            "authorization_code".
        code_verifier (str): Required for clients with PKCE flow when using authorization code. Use together with
            \`grant_type=authorization_code\`. This is the value whose hash was sent as \`code_challenge\` when starting the
            flow.
        grant_type (OAuth2TokenRequestGrantType): The grant type for the token request. Must be "authorization_code" for
            the authorization code flow or "refresh_token" when refreshing an access token.
        redirect_uri (str): The redirect URI that was used in the authorization request. Required when grant_type is
            \`authorization_code\`.
        refresh_token (str): The refresh token from the last grant if the \`offline_access\` scope was included. Use
            together with \`grant_type=refresh_token\`.
        scope (str): A space-separated list of the scopes requested for the access token. Required when grant_type is
            \`refresh_token\`. Must be a subset of the scopes granted during the original authorization.
    """

    code: str
    code_verifier: str
    grant_type: OAuth2TokenRequestGrantType
    redirect_uri: str
    refresh_token: str
    scope: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        code_verifier = self.code_verifier

        grant_type = self.grant_type.value

        redirect_uri = self.redirect_uri

        refresh_token = self.refresh_token

        scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "code_verifier": code_verifier,
                "grant_type": grant_type,
                "redirect_uri": redirect_uri,
                "refresh_token": refresh_token,
                "scope": scope,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        code_verifier = d.pop("code_verifier")

        grant_type = OAuth2TokenRequestGrantType(d.pop("grant_type"))

        redirect_uri = d.pop("redirect_uri")

        refresh_token = d.pop("refresh_token")

        scope = d.pop("scope")

        o_auth_2_token_request = cls(
            code=code,
            code_verifier=code_verifier,
            grant_type=grant_type,
            redirect_uri=redirect_uri,
            refresh_token=refresh_token,
            scope=scope,
        )

        o_auth_2_token_request.additional_properties = d
        return o_auth_2_token_request

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
