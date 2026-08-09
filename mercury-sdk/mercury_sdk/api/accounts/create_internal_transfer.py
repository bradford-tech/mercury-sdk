from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_transfer_api_request import InternalTransferAPIRequest
from ...models.internal_transfer_api_response import InternalTransferAPIResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: InternalTransferAPIRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/transfer",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | InternalTransferAPIResponse | None:
    if response.status_code == 200:
        response_200 = InternalTransferAPIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | InternalTransferAPIResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InternalTransferAPIRequest | Unset = UNSET,
) -> Response[Any | InternalTransferAPIResponse]:
    """Create an internal transfer

     Transfer funds between two accounts within the same organization. Supports transfers between
    depository accounts (checking/savings), from a depository account to a treasury/investment account,
    and from a treasury/investment account to a depository account. Creates paired debit and credit
    transactions.

    Args:
        body (InternalTransferAPIRequest | Unset):  Request body for POST /api/v1/transfer
            endpoint.
             Transfers funds between two depository, treasury, or investment accounts belonging to the
            same organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InternalTransferAPIResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: InternalTransferAPIRequest | Unset = UNSET,
) -> Any | InternalTransferAPIResponse | None:
    """Create an internal transfer

     Transfer funds between two accounts within the same organization. Supports transfers between
    depository accounts (checking/savings), from a depository account to a treasury/investment account,
    and from a treasury/investment account to a depository account. Creates paired debit and credit
    transactions.

    Args:
        body (InternalTransferAPIRequest | Unset):  Request body for POST /api/v1/transfer
            endpoint.
             Transfers funds between two depository, treasury, or investment accounts belonging to the
            same organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InternalTransferAPIResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InternalTransferAPIRequest | Unset = UNSET,
) -> Response[Any | InternalTransferAPIResponse]:
    """Create an internal transfer

     Transfer funds between two accounts within the same organization. Supports transfers between
    depository accounts (checking/savings), from a depository account to a treasury/investment account,
    and from a treasury/investment account to a depository account. Creates paired debit and credit
    transactions.

    Args:
        body (InternalTransferAPIRequest | Unset):  Request body for POST /api/v1/transfer
            endpoint.
             Transfers funds between two depository, treasury, or investment accounts belonging to the
            same organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InternalTransferAPIResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: InternalTransferAPIRequest | Unset = UNSET,
) -> Any | InternalTransferAPIResponse | None:
    """Create an internal transfer

     Transfer funds between two accounts within the same organization. Supports transfers between
    depository accounts (checking/savings), from a depository account to a treasury/investment account,
    and from a treasury/investment account to a depository account. Creates paired debit and credit
    transactions.

    Args:
        body (InternalTransferAPIRequest | Unset):  Request body for POST /api/v1/transfer
            endpoint.
             Transfers funds between two depository, treasury, or investment accounts belonging to the
            same organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InternalTransferAPIResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
