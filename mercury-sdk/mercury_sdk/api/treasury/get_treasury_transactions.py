from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_treasury_transactions_order import GetTreasuryTransactionsOrder
from ...models.treasury_transactions_response import TreasuryTransactionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    treasury_id: UUID,
    *,
    limit: int | Unset = 100,
    order: GetTreasuryTransactionsOrder | Unset = GetTreasuryTransactionsOrder.DESC,
    cursor: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/treasury/{treasury_id}/transactions".format(
            treasury_id=quote(str(treasury_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TreasuryTransactionsResponse | None:
    if response.status_code == 200:
        response_200 = TreasuryTransactionsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | TreasuryTransactionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    treasury_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    order: GetTreasuryTransactionsOrder | Unset = GetTreasuryTransactionsOrder.DESC,
    cursor: int | Unset = UNSET,
) -> Response[Any | TreasuryTransactionsResponse]:
    """Get treasury transactions

     Retrieve paginated treasury transactions for a specific treasury account.

    Args:
        treasury_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Defaults to 100 Default: 100.
        order (GetTreasuryTransactionsOrder | Unset): Sort order for transactions. Can be 'asc' or
            'desc'. Defaults to 'desc' Default: GetTreasuryTransactionsOrder.DESC.
        cursor (int | Unset): Pagination cursor for retrieving next batch of transactions. Must be
            an integer >= 0

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TreasuryTransactionsResponse]
    """

    kwargs = _get_kwargs(
        treasury_id=treasury_id,
        limit=limit,
        order=order,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    treasury_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    order: GetTreasuryTransactionsOrder | Unset = GetTreasuryTransactionsOrder.DESC,
    cursor: int | Unset = UNSET,
) -> Any | TreasuryTransactionsResponse | None:
    """Get treasury transactions

     Retrieve paginated treasury transactions for a specific treasury account.

    Args:
        treasury_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Defaults to 100 Default: 100.
        order (GetTreasuryTransactionsOrder | Unset): Sort order for transactions. Can be 'asc' or
            'desc'. Defaults to 'desc' Default: GetTreasuryTransactionsOrder.DESC.
        cursor (int | Unset): Pagination cursor for retrieving next batch of transactions. Must be
            an integer >= 0

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TreasuryTransactionsResponse
    """

    return sync_detailed(
        treasury_id=treasury_id,
        client=client,
        limit=limit,
        order=order,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    treasury_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    order: GetTreasuryTransactionsOrder | Unset = GetTreasuryTransactionsOrder.DESC,
    cursor: int | Unset = UNSET,
) -> Response[Any | TreasuryTransactionsResponse]:
    """Get treasury transactions

     Retrieve paginated treasury transactions for a specific treasury account.

    Args:
        treasury_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Defaults to 100 Default: 100.
        order (GetTreasuryTransactionsOrder | Unset): Sort order for transactions. Can be 'asc' or
            'desc'. Defaults to 'desc' Default: GetTreasuryTransactionsOrder.DESC.
        cursor (int | Unset): Pagination cursor for retrieving next batch of transactions. Must be
            an integer >= 0

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TreasuryTransactionsResponse]
    """

    kwargs = _get_kwargs(
        treasury_id=treasury_id,
        limit=limit,
        order=order,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    treasury_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    order: GetTreasuryTransactionsOrder | Unset = GetTreasuryTransactionsOrder.DESC,
    cursor: int | Unset = UNSET,
) -> Any | TreasuryTransactionsResponse | None:
    """Get treasury transactions

     Retrieve paginated treasury transactions for a specific treasury account.

    Args:
        treasury_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Defaults to 100 Default: 100.
        order (GetTreasuryTransactionsOrder | Unset): Sort order for transactions. Can be 'asc' or
            'desc'. Defaults to 'desc' Default: GetTreasuryTransactionsOrder.DESC.
        cursor (int | Unset): Pagination cursor for retrieving next batch of transactions. Must be
            an integer >= 0

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TreasuryTransactionsResponse
    """

    return (
        await asyncio_detailed(
            treasury_id=treasury_id,
            client=client,
            limit=limit,
            order=order,
            cursor=cursor,
        )
    ).parsed
