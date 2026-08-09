from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client_id: str,
    redirect_uri: str,
    scope: str | Unset = UNSET,
    state: str | Unset = UNSET,
    response_type: str,
    code_challenge: str | Unset = UNSET,
    code_challenge_method: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["client_id"] = client_id

    params["redirect_uri"] = redirect_uri

    params["scope"] = scope

    params["state"] = state

    params["response_type"] = response_type

    params["code_challenge"] = code_challenge

    params["code_challenge_method"] = code_challenge_method

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/oauth2/auth",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 302:
        return None

    if response.status_code == 400:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    client_id: str,
    redirect_uri: str,
    scope: str | Unset = UNSET,
    state: str | Unset = UNSET,
    response_type: str,
    code_challenge: str | Unset = UNSET,
    code_challenge_method: str | Unset = UNSET,
) -> Response[Any]:
    """Start OAuth2 web flow

     Initiates the OAuth2 authorization flow. Redirects the user to Mercury's consent page.

    Args:
        client_id (str):
        redirect_uri (str):
        scope (str | Unset):
        state (str | Unset):
        response_type (str):
        code_challenge (str | Unset):
        code_challenge_method (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        redirect_uri=redirect_uri,
        scope=scope,
        state=state,
        response_type=response_type,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    client_id: str,
    redirect_uri: str,
    scope: str | Unset = UNSET,
    state: str | Unset = UNSET,
    response_type: str,
    code_challenge: str | Unset = UNSET,
    code_challenge_method: str | Unset = UNSET,
) -> Response[Any]:
    """Start OAuth2 web flow

     Initiates the OAuth2 authorization flow. Redirects the user to Mercury's consent page.

    Args:
        client_id (str):
        redirect_uri (str):
        scope (str | Unset):
        state (str | Unset):
        response_type (str):
        code_challenge (str | Unset):
        code_challenge_method (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        redirect_uri=redirect_uri,
        scope=scope,
        state=state,
        response_type=response_type,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
