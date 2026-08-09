from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.recipient_info import RecipientInfo
from ...types import Response


def _get_kwargs(
    recipient_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/recipient/{recipient_id}".format(
            recipient_id=quote(str(recipient_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RecipientInfo | None:
    if response.status_code == 200:
        response_200 = RecipientInfo.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | RecipientInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    recipient_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RecipientInfo]:
    """Get recipient by ID

     Retrieve details of a specific recipient by ID

    Args:
        recipient_id (UUID): ID for a Mercury account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RecipientInfo]
    """

    kwargs = _get_kwargs(
        recipient_id=recipient_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    recipient_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RecipientInfo | None:
    """Get recipient by ID

     Retrieve details of a specific recipient by ID

    Args:
        recipient_id (UUID): ID for a Mercury account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RecipientInfo
    """

    return sync_detailed(
        recipient_id=recipient_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    recipient_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RecipientInfo]:
    """Get recipient by ID

     Retrieve details of a specific recipient by ID

    Args:
        recipient_id (UUID): ID for a Mercury account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RecipientInfo]
    """

    kwargs = _get_kwargs(
        recipient_id=recipient_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    recipient_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RecipientInfo | None:
    """Get recipient by ID

     Retrieve details of a specific recipient by ID

    Args:
        recipient_id (UUID): ID for a Mercury account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RecipientInfo
    """

    return (
        await asyncio_detailed(
            recipient_id=recipient_id,
            client=client,
        )
    ).parsed
