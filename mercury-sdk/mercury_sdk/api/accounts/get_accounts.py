from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.accounts_paginated_response import AccountsPaginatedResponse
from ...models.get_accounts_order import GetAccountsOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 1000,
    order: GetAccountsOrder | Unset = GetAccountsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    json_start_after: str | Unset = UNSET
    if not isinstance(start_after, Unset):
        json_start_after = str(start_after)
    params["start_after"] = json_start_after

    json_end_before: str | Unset = UNSET
    if not isinstance(end_before, Unset):
        json_end_before = str(end_before)
    params["end_before"] = json_end_before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountsPaginatedResponse | Any | None:
    if response.status_code == 200:
        response_200 = AccountsPaginatedResponse.from_dict(response.json())

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
) -> Response[AccountsPaginatedResponse | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    order: GetAccountsOrder | Unset = GetAccountsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
) -> Response[AccountsPaginatedResponse | Any]:
    """Get all accounts

     Retrieve a paginated list of accounts. Supports cursor-based pagination with limit, order,
    start_after, and end_before query parameters.

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (GetAccountsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to 'asc'
            Default: GetAccountsOrder.ASC.
        start_after (UUID | Unset): The ID of the account to start the page after (exclusive).
            When provided, results will begin with the account immediately following this ID. Use this
            for standard forward pagination to get the next page of results. Cannot be combined with
            end_before.
        end_before (UUID | Unset): The ID of the account to end the page before (exclusive). When
            provided, results will end just before this ID and work backwards. Use this for reverse
            pagination or to retrieve previous pages. Cannot be combined with start_after.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountsPaginatedResponse | Any]
    """

    kwargs = _get_kwargs(
        limit=limit,
        order=order,
        start_after=start_after,
        end_before=end_before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    order: GetAccountsOrder | Unset = GetAccountsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
) -> AccountsPaginatedResponse | Any | None:
    """Get all accounts

     Retrieve a paginated list of accounts. Supports cursor-based pagination with limit, order,
    start_after, and end_before query parameters.

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (GetAccountsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to 'asc'
            Default: GetAccountsOrder.ASC.
        start_after (UUID | Unset): The ID of the account to start the page after (exclusive).
            When provided, results will begin with the account immediately following this ID. Use this
            for standard forward pagination to get the next page of results. Cannot be combined with
            end_before.
        end_before (UUID | Unset): The ID of the account to end the page before (exclusive). When
            provided, results will end just before this ID and work backwards. Use this for reverse
            pagination or to retrieve previous pages. Cannot be combined with start_after.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountsPaginatedResponse | Any
    """

    return sync_detailed(
        client=client,
        limit=limit,
        order=order,
        start_after=start_after,
        end_before=end_before,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    order: GetAccountsOrder | Unset = GetAccountsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
) -> Response[AccountsPaginatedResponse | Any]:
    """Get all accounts

     Retrieve a paginated list of accounts. Supports cursor-based pagination with limit, order,
    start_after, and end_before query parameters.

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (GetAccountsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to 'asc'
            Default: GetAccountsOrder.ASC.
        start_after (UUID | Unset): The ID of the account to start the page after (exclusive).
            When provided, results will begin with the account immediately following this ID. Use this
            for standard forward pagination to get the next page of results. Cannot be combined with
            end_before.
        end_before (UUID | Unset): The ID of the account to end the page before (exclusive). When
            provided, results will end just before this ID and work backwards. Use this for reverse
            pagination or to retrieve previous pages. Cannot be combined with start_after.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountsPaginatedResponse | Any]
    """

    kwargs = _get_kwargs(
        limit=limit,
        order=order,
        start_after=start_after,
        end_before=end_before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    order: GetAccountsOrder | Unset = GetAccountsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
) -> AccountsPaginatedResponse | Any | None:
    """Get all accounts

     Retrieve a paginated list of accounts. Supports cursor-based pagination with limit, order,
    start_after, and end_before query parameters.

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (GetAccountsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to 'asc'
            Default: GetAccountsOrder.ASC.
        start_after (UUID | Unset): The ID of the account to start the page after (exclusive).
            When provided, results will begin with the account immediately following this ID. Use this
            for standard forward pagination to get the next page of results. Cannot be combined with
            end_before.
        end_before (UUID | Unset): The ID of the account to end the page before (exclusive). When
            provided, results will end just before this ID and work backwards. Use this for reverse
            pagination or to retrieve previous pages. Cannot be combined with start_after.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountsPaginatedResponse | Any
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
        )
    ).parsed
