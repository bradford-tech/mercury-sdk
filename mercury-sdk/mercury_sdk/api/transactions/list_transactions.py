from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_transactions_order import ListTransactionsOrder
from ...models.list_transactions_status_item import ListTransactionsStatusItem
from ...models.transactions_paginated_response import TransactionsPaginatedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: list[ListTransactionsStatusItem] | Unset = UNSET,
    search: str | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    posted_start: str | Unset = UNSET,
    posted_end: str | Unset = UNSET,
    account_id: list[UUID] | Unset = UNSET,
    card_id: list[str] | Unset = UNSET,
    mercury_category: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    start_at: str | Unset = UNSET,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    limit: int | Unset = 1000,
    order: ListTransactionsOrder | Unset = ListTransactionsOrder.ASC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params["search"] = search

    params["start"] = start

    params["end"] = end

    params["postedStart"] = posted_start

    params["postedEnd"] = posted_end

    json_account_id: list[str] | Unset = UNSET
    if not isinstance(account_id, Unset):
        json_account_id = []
        for account_id_item_data in account_id:
            account_id_item = str(account_id_item_data)
            json_account_id.append(account_id_item)

    params["accountId"] = json_account_id

    json_card_id: list[str] | Unset = UNSET
    if not isinstance(card_id, Unset):
        json_card_id = card_id

    params["cardId"] = json_card_id

    params["mercuryCategory"] = mercury_category

    params["categoryId"] = category_id

    params["start_at"] = start_at

    json_start_after: str | Unset = UNSET
    if not isinstance(start_after, Unset):
        json_start_after = str(start_after)
    params["start_after"] = json_start_after

    json_end_before: str | Unset = UNSET
    if not isinstance(end_before, Unset):
        json_end_before = str(end_before)
    params["end_before"] = json_end_before

    params["limit"] = limit

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/transactions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TransactionsPaginatedResponse | None:
    if response.status_code == 200:
        response_200 = TransactionsPaginatedResponse.from_dict(response.json())

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
) -> Response[Any | TransactionsPaginatedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: list[ListTransactionsStatusItem] | Unset = UNSET,
    search: str | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    posted_start: str | Unset = UNSET,
    posted_end: str | Unset = UNSET,
    account_id: list[UUID] | Unset = UNSET,
    card_id: list[str] | Unset = UNSET,
    mercury_category: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    start_at: str | Unset = UNSET,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    limit: int | Unset = 1000,
    order: ListTransactionsOrder | Unset = ListTransactionsOrder.ASC,
) -> Response[Any | TransactionsPaginatedResponse]:
    """List all transactions

     Retrieve a paginated list of all transactions across all accounts. Supports advanced filtering by
    date ranges, status, categories, and cursor-based pagination.

    Args:
        status (list[ListTransactionsStatusItem] | Unset):
        search (str | Unset): Search term to look for in transaction descriptions.
        start (str | Unset): Earliest createdAt date to filter for. If not provided, it defaults
            to the date of your first transaction. Format: YYYY-MM-DD or an ISO 8601 string. Please
            note that your Mercury transactions on your Dashboard might have their postedAt date
            displayed, as opposed to createdAt
        end (str | Unset): Latest createdAt date to filter for. If it’s not provided, it defaults
            to current day. Format: YYYY-MM-DD or an ISO 8601 string. Please note that your Mercury
            transactions on your Dashboard might have their postedAt date displayed, as opposed to
            createdAt
        posted_start (str | Unset): Earliest postedAt date to filter for. Format: YYYY-MM-DD or an
            ISO 8601 string
        posted_end (str | Unset): Latest postedAt date to filter for. Format: YYYY-MM-DD or an ISO
            8601 string
        account_id (list[UUID] | Unset):
        card_id (list[str] | Unset):
        mercury_category (str | Unset): Name of mercuryCategory you want to filter on. Merchant
            Type in the UI.
        category_id (str | Unset): UUID of a custom category. Can be returned from /categories
            endpoint.
        start_at (str | Unset): The ID of the resource to start the page at (inclusive). When
            provided, results will begin with and include the resource with this ID. Use this to
            retrieve a specific page when you know the exact starting point. Cannot be combined with
            start_after or end_before.
        start_after (UUID | Unset): The ID of the transaction to start the page after (exclusive).
            When provided, results will begin with the transaction immediately following this ID. Use
            this for standard forward pagination to get the next page of results. Cannot be combined
            with end_before.
        end_before (UUID | Unset): The ID of the transaction to end the page before (exclusive).
            When provided, results will end just before this ID and work backwards. Use this for
            reverse pagination or to retrieve previous pages. Cannot be combined with start_after.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (ListTransactionsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to
            'asc' Default: ListTransactionsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TransactionsPaginatedResponse]
    """

    kwargs = _get_kwargs(
        status=status,
        search=search,
        start=start,
        end=end,
        posted_start=posted_start,
        posted_end=posted_end,
        account_id=account_id,
        card_id=card_id,
        mercury_category=mercury_category,
        category_id=category_id,
        start_at=start_at,
        start_after=start_after,
        end_before=end_before,
        limit=limit,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    status: list[ListTransactionsStatusItem] | Unset = UNSET,
    search: str | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    posted_start: str | Unset = UNSET,
    posted_end: str | Unset = UNSET,
    account_id: list[UUID] | Unset = UNSET,
    card_id: list[str] | Unset = UNSET,
    mercury_category: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    start_at: str | Unset = UNSET,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    limit: int | Unset = 1000,
    order: ListTransactionsOrder | Unset = ListTransactionsOrder.ASC,
) -> Any | TransactionsPaginatedResponse | None:
    """List all transactions

     Retrieve a paginated list of all transactions across all accounts. Supports advanced filtering by
    date ranges, status, categories, and cursor-based pagination.

    Args:
        status (list[ListTransactionsStatusItem] | Unset):
        search (str | Unset): Search term to look for in transaction descriptions.
        start (str | Unset): Earliest createdAt date to filter for. If not provided, it defaults
            to the date of your first transaction. Format: YYYY-MM-DD or an ISO 8601 string. Please
            note that your Mercury transactions on your Dashboard might have their postedAt date
            displayed, as opposed to createdAt
        end (str | Unset): Latest createdAt date to filter for. If it’s not provided, it defaults
            to current day. Format: YYYY-MM-DD or an ISO 8601 string. Please note that your Mercury
            transactions on your Dashboard might have their postedAt date displayed, as opposed to
            createdAt
        posted_start (str | Unset): Earliest postedAt date to filter for. Format: YYYY-MM-DD or an
            ISO 8601 string
        posted_end (str | Unset): Latest postedAt date to filter for. Format: YYYY-MM-DD or an ISO
            8601 string
        account_id (list[UUID] | Unset):
        card_id (list[str] | Unset):
        mercury_category (str | Unset): Name of mercuryCategory you want to filter on. Merchant
            Type in the UI.
        category_id (str | Unset): UUID of a custom category. Can be returned from /categories
            endpoint.
        start_at (str | Unset): The ID of the resource to start the page at (inclusive). When
            provided, results will begin with and include the resource with this ID. Use this to
            retrieve a specific page when you know the exact starting point. Cannot be combined with
            start_after or end_before.
        start_after (UUID | Unset): The ID of the transaction to start the page after (exclusive).
            When provided, results will begin with the transaction immediately following this ID. Use
            this for standard forward pagination to get the next page of results. Cannot be combined
            with end_before.
        end_before (UUID | Unset): The ID of the transaction to end the page before (exclusive).
            When provided, results will end just before this ID and work backwards. Use this for
            reverse pagination or to retrieve previous pages. Cannot be combined with start_after.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (ListTransactionsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to
            'asc' Default: ListTransactionsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TransactionsPaginatedResponse
    """

    return sync_detailed(
        client=client,
        status=status,
        search=search,
        start=start,
        end=end,
        posted_start=posted_start,
        posted_end=posted_end,
        account_id=account_id,
        card_id=card_id,
        mercury_category=mercury_category,
        category_id=category_id,
        start_at=start_at,
        start_after=start_after,
        end_before=end_before,
        limit=limit,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: list[ListTransactionsStatusItem] | Unset = UNSET,
    search: str | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    posted_start: str | Unset = UNSET,
    posted_end: str | Unset = UNSET,
    account_id: list[UUID] | Unset = UNSET,
    card_id: list[str] | Unset = UNSET,
    mercury_category: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    start_at: str | Unset = UNSET,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    limit: int | Unset = 1000,
    order: ListTransactionsOrder | Unset = ListTransactionsOrder.ASC,
) -> Response[Any | TransactionsPaginatedResponse]:
    """List all transactions

     Retrieve a paginated list of all transactions across all accounts. Supports advanced filtering by
    date ranges, status, categories, and cursor-based pagination.

    Args:
        status (list[ListTransactionsStatusItem] | Unset):
        search (str | Unset): Search term to look for in transaction descriptions.
        start (str | Unset): Earliest createdAt date to filter for. If not provided, it defaults
            to the date of your first transaction. Format: YYYY-MM-DD or an ISO 8601 string. Please
            note that your Mercury transactions on your Dashboard might have their postedAt date
            displayed, as opposed to createdAt
        end (str | Unset): Latest createdAt date to filter for. If it’s not provided, it defaults
            to current day. Format: YYYY-MM-DD or an ISO 8601 string. Please note that your Mercury
            transactions on your Dashboard might have their postedAt date displayed, as opposed to
            createdAt
        posted_start (str | Unset): Earliest postedAt date to filter for. Format: YYYY-MM-DD or an
            ISO 8601 string
        posted_end (str | Unset): Latest postedAt date to filter for. Format: YYYY-MM-DD or an ISO
            8601 string
        account_id (list[UUID] | Unset):
        card_id (list[str] | Unset):
        mercury_category (str | Unset): Name of mercuryCategory you want to filter on. Merchant
            Type in the UI.
        category_id (str | Unset): UUID of a custom category. Can be returned from /categories
            endpoint.
        start_at (str | Unset): The ID of the resource to start the page at (inclusive). When
            provided, results will begin with and include the resource with this ID. Use this to
            retrieve a specific page when you know the exact starting point. Cannot be combined with
            start_after or end_before.
        start_after (UUID | Unset): The ID of the transaction to start the page after (exclusive).
            When provided, results will begin with the transaction immediately following this ID. Use
            this for standard forward pagination to get the next page of results. Cannot be combined
            with end_before.
        end_before (UUID | Unset): The ID of the transaction to end the page before (exclusive).
            When provided, results will end just before this ID and work backwards. Use this for
            reverse pagination or to retrieve previous pages. Cannot be combined with start_after.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (ListTransactionsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to
            'asc' Default: ListTransactionsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TransactionsPaginatedResponse]
    """

    kwargs = _get_kwargs(
        status=status,
        search=search,
        start=start,
        end=end,
        posted_start=posted_start,
        posted_end=posted_end,
        account_id=account_id,
        card_id=card_id,
        mercury_category=mercury_category,
        category_id=category_id,
        start_at=start_at,
        start_after=start_after,
        end_before=end_before,
        limit=limit,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: list[ListTransactionsStatusItem] | Unset = UNSET,
    search: str | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    posted_start: str | Unset = UNSET,
    posted_end: str | Unset = UNSET,
    account_id: list[UUID] | Unset = UNSET,
    card_id: list[str] | Unset = UNSET,
    mercury_category: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    start_at: str | Unset = UNSET,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    limit: int | Unset = 1000,
    order: ListTransactionsOrder | Unset = ListTransactionsOrder.ASC,
) -> Any | TransactionsPaginatedResponse | None:
    """List all transactions

     Retrieve a paginated list of all transactions across all accounts. Supports advanced filtering by
    date ranges, status, categories, and cursor-based pagination.

    Args:
        status (list[ListTransactionsStatusItem] | Unset):
        search (str | Unset): Search term to look for in transaction descriptions.
        start (str | Unset): Earliest createdAt date to filter for. If not provided, it defaults
            to the date of your first transaction. Format: YYYY-MM-DD or an ISO 8601 string. Please
            note that your Mercury transactions on your Dashboard might have their postedAt date
            displayed, as opposed to createdAt
        end (str | Unset): Latest createdAt date to filter for. If it’s not provided, it defaults
            to current day. Format: YYYY-MM-DD or an ISO 8601 string. Please note that your Mercury
            transactions on your Dashboard might have their postedAt date displayed, as opposed to
            createdAt
        posted_start (str | Unset): Earliest postedAt date to filter for. Format: YYYY-MM-DD or an
            ISO 8601 string
        posted_end (str | Unset): Latest postedAt date to filter for. Format: YYYY-MM-DD or an ISO
            8601 string
        account_id (list[UUID] | Unset):
        card_id (list[str] | Unset):
        mercury_category (str | Unset): Name of mercuryCategory you want to filter on. Merchant
            Type in the UI.
        category_id (str | Unset): UUID of a custom category. Can be returned from /categories
            endpoint.
        start_at (str | Unset): The ID of the resource to start the page at (inclusive). When
            provided, results will begin with and include the resource with this ID. Use this to
            retrieve a specific page when you know the exact starting point. Cannot be combined with
            start_after or end_before.
        start_after (UUID | Unset): The ID of the transaction to start the page after (exclusive).
            When provided, results will begin with the transaction immediately following this ID. Use
            this for standard forward pagination to get the next page of results. Cannot be combined
            with end_before.
        end_before (UUID | Unset): The ID of the transaction to end the page before (exclusive).
            When provided, results will end just before this ID and work backwards. Use this for
            reverse pagination or to retrieve previous pages. Cannot be combined with start_after.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (ListTransactionsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to
            'asc' Default: ListTransactionsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TransactionsPaginatedResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            search=search,
            start=start,
            end=end,
            posted_start=posted_start,
            posted_end=posted_end,
            account_id=account_id,
            card_id=card_id,
            mercury_category=mercury_category,
            category_id=category_id,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            limit=limit,
            order=order,
        )
    ).parsed
