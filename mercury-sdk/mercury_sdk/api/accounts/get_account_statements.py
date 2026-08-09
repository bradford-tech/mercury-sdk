from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.depository_account_statements_paginated_response import DepositoryAccountStatementsPaginatedResponse
from ...models.get_account_statements_order import GetAccountStatementsOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: UUID,
    *,
    limit: int | Unset = 1000,
    order: GetAccountStatementsOrder | Unset = GetAccountStatementsOrder.DESC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
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

    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/account/{account_id}/statements".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DepositoryAccountStatementsPaginatedResponse | None:
    if response.status_code == 200:
        response_200 = DepositoryAccountStatementsPaginatedResponse.from_dict(response.json())

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
) -> Response[Any | DepositoryAccountStatementsPaginatedResponse]:
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
    order: GetAccountStatementsOrder | Unset = GetAccountStatementsOrder.DESC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Response[Any | DepositoryAccountStatementsPaginatedResponse]:
    """Get account statements

     Retrieve a paginated list of monthly statements for a specific account. Supports cursor-based
    pagination with limit, order, start_after, and end_before query parameters, as well as date range
    filtering with start and end parameters.

    Args:
        account_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (GetAccountStatementsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to
            'desc' Default: GetAccountStatementsOrder.DESC.
        start_after (UUID | Unset): The ID of the statement to start the page after (exclusive).
            When provided, results will begin with the statement immediately following this ID. Use
            this for standard forward pagination to get the next page of results. Cannot be combined
            with end_before.
        end_before (UUID | Unset): The ID of the statement to end the page before (exclusive).
            When provided, results will end just before this ID and work backwards. Use this for
            reverse pagination or to retrieve previous pages. Cannot be combined with start_after.
        start (str | Unset): Filter statements where the period start date is on or after this
            date. Format: YYYY-MM-DD
        end (str | Unset): Filter statements where the period start date is on or before this
            date. If the date is in the future, defaults to the current date. Format: YYYY-MM-DD

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DepositoryAccountStatementsPaginatedResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        limit=limit,
        order=order,
        start_after=start_after,
        end_before=end_before,
        start=start,
        end=end,
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
    order: GetAccountStatementsOrder | Unset = GetAccountStatementsOrder.DESC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Any | DepositoryAccountStatementsPaginatedResponse | None:
    """Get account statements

     Retrieve a paginated list of monthly statements for a specific account. Supports cursor-based
    pagination with limit, order, start_after, and end_before query parameters, as well as date range
    filtering with start and end parameters.

    Args:
        account_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (GetAccountStatementsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to
            'desc' Default: GetAccountStatementsOrder.DESC.
        start_after (UUID | Unset): The ID of the statement to start the page after (exclusive).
            When provided, results will begin with the statement immediately following this ID. Use
            this for standard forward pagination to get the next page of results. Cannot be combined
            with end_before.
        end_before (UUID | Unset): The ID of the statement to end the page before (exclusive).
            When provided, results will end just before this ID and work backwards. Use this for
            reverse pagination or to retrieve previous pages. Cannot be combined with start_after.
        start (str | Unset): Filter statements where the period start date is on or after this
            date. Format: YYYY-MM-DD
        end (str | Unset): Filter statements where the period start date is on or before this
            date. If the date is in the future, defaults to the current date. Format: YYYY-MM-DD

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DepositoryAccountStatementsPaginatedResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        limit=limit,
        order=order,
        start_after=start_after,
        end_before=end_before,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    order: GetAccountStatementsOrder | Unset = GetAccountStatementsOrder.DESC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Response[Any | DepositoryAccountStatementsPaginatedResponse]:
    """Get account statements

     Retrieve a paginated list of monthly statements for a specific account. Supports cursor-based
    pagination with limit, order, start_after, and end_before query parameters, as well as date range
    filtering with start and end parameters.

    Args:
        account_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (GetAccountStatementsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to
            'desc' Default: GetAccountStatementsOrder.DESC.
        start_after (UUID | Unset): The ID of the statement to start the page after (exclusive).
            When provided, results will begin with the statement immediately following this ID. Use
            this for standard forward pagination to get the next page of results. Cannot be combined
            with end_before.
        end_before (UUID | Unset): The ID of the statement to end the page before (exclusive).
            When provided, results will end just before this ID and work backwards. Use this for
            reverse pagination or to retrieve previous pages. Cannot be combined with start_after.
        start (str | Unset): Filter statements where the period start date is on or after this
            date. Format: YYYY-MM-DD
        end (str | Unset): Filter statements where the period start date is on or before this
            date. If the date is in the future, defaults to the current date. Format: YYYY-MM-DD

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DepositoryAccountStatementsPaginatedResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        limit=limit,
        order=order,
        start_after=start_after,
        end_before=end_before,
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    order: GetAccountStatementsOrder | Unset = GetAccountStatementsOrder.DESC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Any | DepositoryAccountStatementsPaginatedResponse | None:
    """Get account statements

     Retrieve a paginated list of monthly statements for a specific account. Supports cursor-based
    pagination with limit, order, start_after, and end_before query parameters, as well as date range
    filtering with start and end parameters.

    Args:
        account_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (GetAccountStatementsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to
            'desc' Default: GetAccountStatementsOrder.DESC.
        start_after (UUID | Unset): The ID of the statement to start the page after (exclusive).
            When provided, results will begin with the statement immediately following this ID. Use
            this for standard forward pagination to get the next page of results. Cannot be combined
            with end_before.
        end_before (UUID | Unset): The ID of the statement to end the page before (exclusive).
            When provided, results will end just before this ID and work backwards. Use this for
            reverse pagination or to retrieve previous pages. Cannot be combined with start_after.
        start (str | Unset): Filter statements where the period start date is on or after this
            date. Format: YYYY-MM-DD
        end (str | Unset): Filter statements where the period start date is on or before this
            date. If the date is in the future, defaults to the current date. Format: YYYY-MM-DD

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DepositoryAccountStatementsPaginatedResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
            start=start,
            end=end,
        )
    ).parsed
