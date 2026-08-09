from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_account_transactions_order import ListAccountTransactionsOrder
from ...models.list_account_transactions_status import ListAccountTransactionsStatus
from ...models.transactions_response import TransactionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: UUID,
    *,
    limit: int | Unset = 1000,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: ListAccountTransactionsStatus | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: ListAccountTransactionsOrder | Unset = ListAccountTransactionsOrder.DESC,
    request_id: UUID | Unset = UNSET,
    mercury_category: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["start"] = start

    params["end"] = end

    params["search"] = search

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["offset"] = offset

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    json_request_id: str | Unset = UNSET
    if not isinstance(request_id, Unset):
        json_request_id = str(request_id)
    params["requestId"] = json_request_id

    params["mercuryCategory"] = mercury_category

    json_category_id: str | Unset = UNSET
    if not isinstance(category_id, Unset):
        json_category_id = str(category_id)
    params["categoryId"] = json_category_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/account/{account_id}/transactions".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TransactionsResponse | None:
    if response.status_code == 200:
        response_200 = TransactionsResponse.from_dict(response.json())

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
) -> Response[Any | TransactionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: ListAccountTransactionsStatus | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: ListAccountTransactionsOrder | Unset = ListAccountTransactionsOrder.DESC,
    request_id: UUID | Unset = UNSET,
    mercury_category: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,
) -> Response[Any | TransactionsResponse]:
    """List account transactions

     Retrieve a paginated list of transactions for a specific account. Supports filtering by date range,
    status, and search terms.

    Args:
        account_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start (str | Unset): Earliest date to filter transactions. If not provided, defaults to 30
            days before the current date. Format: YYYY-MM-DD or ISO 8601 string
        end (str | Unset): Latest date to filter transactions. If not provided, defaults to the
            current date. Format: YYYY-MM-DD or ISO 8601 string
        search (str | Unset): Search term to filter transactions by description or counterparty
            name
        status (ListAccountTransactionsStatus | Unset):
        offset (int | Unset): Number of results to skip for pagination
        order (ListAccountTransactionsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults
            to 'desc' Default: ListAccountTransactionsOrder.DESC.
        request_id (UUID | Unset): ID returned from /account/:id/request-send-money
        mercury_category (str | Unset): Name of mercuryCategory you want to filter on. Merchant
            Type in the UI.
        category_id (UUID | Unset): UUID of a custom category. Can be returned from /categories
            endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TransactionsResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        limit=limit,
        start=start,
        end=end,
        search=search,
        status=status,
        offset=offset,
        order=order,
        request_id=request_id,
        mercury_category=mercury_category,
        category_id=category_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: ListAccountTransactionsStatus | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: ListAccountTransactionsOrder | Unset = ListAccountTransactionsOrder.DESC,
    request_id: UUID | Unset = UNSET,
    mercury_category: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,
) -> Any | TransactionsResponse | None:
    """List account transactions

     Retrieve a paginated list of transactions for a specific account. Supports filtering by date range,
    status, and search terms.

    Args:
        account_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start (str | Unset): Earliest date to filter transactions. If not provided, defaults to 30
            days before the current date. Format: YYYY-MM-DD or ISO 8601 string
        end (str | Unset): Latest date to filter transactions. If not provided, defaults to the
            current date. Format: YYYY-MM-DD or ISO 8601 string
        search (str | Unset): Search term to filter transactions by description or counterparty
            name
        status (ListAccountTransactionsStatus | Unset):
        offset (int | Unset): Number of results to skip for pagination
        order (ListAccountTransactionsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults
            to 'desc' Default: ListAccountTransactionsOrder.DESC.
        request_id (UUID | Unset): ID returned from /account/:id/request-send-money
        mercury_category (str | Unset): Name of mercuryCategory you want to filter on. Merchant
            Type in the UI.
        category_id (UUID | Unset): UUID of a custom category. Can be returned from /categories
            endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TransactionsResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        limit=limit,
        start=start,
        end=end,
        search=search,
        status=status,
        offset=offset,
        order=order,
        request_id=request_id,
        mercury_category=mercury_category,
        category_id=category_id,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: ListAccountTransactionsStatus | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: ListAccountTransactionsOrder | Unset = ListAccountTransactionsOrder.DESC,
    request_id: UUID | Unset = UNSET,
    mercury_category: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,
) -> Response[Any | TransactionsResponse]:
    """List account transactions

     Retrieve a paginated list of transactions for a specific account. Supports filtering by date range,
    status, and search terms.

    Args:
        account_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start (str | Unset): Earliest date to filter transactions. If not provided, defaults to 30
            days before the current date. Format: YYYY-MM-DD or ISO 8601 string
        end (str | Unset): Latest date to filter transactions. If not provided, defaults to the
            current date. Format: YYYY-MM-DD or ISO 8601 string
        search (str | Unset): Search term to filter transactions by description or counterparty
            name
        status (ListAccountTransactionsStatus | Unset):
        offset (int | Unset): Number of results to skip for pagination
        order (ListAccountTransactionsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults
            to 'desc' Default: ListAccountTransactionsOrder.DESC.
        request_id (UUID | Unset): ID returned from /account/:id/request-send-money
        mercury_category (str | Unset): Name of mercuryCategory you want to filter on. Merchant
            Type in the UI.
        category_id (UUID | Unset): UUID of a custom category. Can be returned from /categories
            endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TransactionsResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        limit=limit,
        start=start,
        end=end,
        search=search,
        status=status,
        offset=offset,
        order=order,
        request_id=request_id,
        mercury_category=mercury_category,
        category_id=category_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: ListAccountTransactionsStatus | Unset = UNSET,
    offset: int | Unset = UNSET,
    order: ListAccountTransactionsOrder | Unset = ListAccountTransactionsOrder.DESC,
    request_id: UUID | Unset = UNSET,
    mercury_category: str | Unset = UNSET,
    category_id: UUID | Unset = UNSET,
) -> Any | TransactionsResponse | None:
    """List account transactions

     Retrieve a paginated list of transactions for a specific account. Supports filtering by date range,
    status, and search terms.

    Args:
        account_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start (str | Unset): Earliest date to filter transactions. If not provided, defaults to 30
            days before the current date. Format: YYYY-MM-DD or ISO 8601 string
        end (str | Unset): Latest date to filter transactions. If not provided, defaults to the
            current date. Format: YYYY-MM-DD or ISO 8601 string
        search (str | Unset): Search term to filter transactions by description or counterparty
            name
        status (ListAccountTransactionsStatus | Unset):
        offset (int | Unset): Number of results to skip for pagination
        order (ListAccountTransactionsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults
            to 'desc' Default: ListAccountTransactionsOrder.DESC.
        request_id (UUID | Unset): ID returned from /account/:id/request-send-money
        mercury_category (str | Unset): Name of mercuryCategory you want to filter on. Merchant
            Type in the UI.
        category_id (UUID | Unset): UUID of a custom category. Can be returned from /categories
            endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TransactionsResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            limit=limit,
            start=start,
            end=end,
            search=search,
            status=status,
            offset=offset,
            order=order,
            request_id=request_id,
            mercury_category=mercury_category,
            category_id=category_id,
        )
    ).parsed
