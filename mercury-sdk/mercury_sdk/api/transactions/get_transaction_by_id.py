from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transaction import Transaction
from ...types import Response


def _get_kwargs(
    transaction_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/transaction/{transaction_id}".format(
            transaction_id=quote(str(transaction_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Transaction | None:
    if response.status_code == 200:
        response_200 = Transaction.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Transaction]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transaction_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Transaction]:
    """Get a transaction by ID

     Retrieve a single transaction by its ID. Returns full transaction details including attachments,
    check images, and related metadata.

    Args:
        transaction_id (UUID): ID for this transaction

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Transaction]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transaction_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Transaction | None:
    """Get a transaction by ID

     Retrieve a single transaction by its ID. Returns full transaction details including attachments,
    check images, and related metadata.

    Args:
        transaction_id (UUID): ID for this transaction

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Transaction
    """

    return sync_detailed(
        transaction_id=transaction_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    transaction_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Transaction]:
    """Get a transaction by ID

     Retrieve a single transaction by its ID. Returns full transaction details including attachments,
    check images, and related metadata.

    Args:
        transaction_id (UUID): ID for this transaction

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Transaction]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transaction_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Transaction | None:
    """Get a transaction by ID

     Retrieve a single transaction by its ID. Returns full transaction details including attachments,
    check images, and related metadata.

    Args:
        transaction_id (UUID): ID for this transaction

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Transaction
    """

    return (
        await asyncio_detailed(
            transaction_id=transaction_id,
            client=client,
        )
    ).parsed
