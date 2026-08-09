from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_safe_request import APISafeRequest
from ...types import Response


def _get_kwargs(
    safe_request_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/safes/{safe_request_id}".format(
            safe_request_id=quote(str(safe_request_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> APISafeRequest | Any | None:
    if response.status_code == 200:
        response_200 = APISafeRequest.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APISafeRequest | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    safe_request_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[APISafeRequest | Any]:
    """Get SAFE by ID

     Retrieve a specific SAFE request by its ID.

    Args:
        safe_request_id (UUID): ID for the SAFE request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APISafeRequest | Any]
    """

    kwargs = _get_kwargs(
        safe_request_id=safe_request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    safe_request_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> APISafeRequest | Any | None:
    """Get SAFE by ID

     Retrieve a specific SAFE request by its ID.

    Args:
        safe_request_id (UUID): ID for the SAFE request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APISafeRequest | Any
    """

    return sync_detailed(
        safe_request_id=safe_request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    safe_request_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[APISafeRequest | Any]:
    """Get SAFE by ID

     Retrieve a specific SAFE request by its ID.

    Args:
        safe_request_id (UUID): ID for the SAFE request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APISafeRequest | Any]
    """

    kwargs = _get_kwargs(
        safe_request_id=safe_request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    safe_request_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> APISafeRequest | Any | None:
    """Get SAFE by ID

     Retrieve a specific SAFE request by its ID.

    Args:
        safe_request_id (UUID): ID for the SAFE request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APISafeRequest | Any
    """

    return (
        await asyncio_detailed(
            safe_request_id=safe_request_id,
            client=client,
        )
    ).parsed
