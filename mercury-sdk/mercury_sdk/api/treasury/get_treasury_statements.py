from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_treasury_statements_document_type import GetTreasuryStatementsDocumentType
from ...models.get_treasury_statements_order import GetTreasuryStatementsOrder
from ...models.treasury_statements_paginated_response import TreasuryStatementsPaginatedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    treasury_id: UUID,
    *,
    limit: int | Unset = 1000,
    order: GetTreasuryStatementsOrder | Unset = GetTreasuryStatementsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    document_type: GetTreasuryStatementsDocumentType | Unset = UNSET,
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

    json_document_type: str | Unset = UNSET
    if not isinstance(document_type, Unset):
        json_document_type = document_type.value

    params["documentType"] = json_document_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/treasury/{treasury_id}/statements".format(
            treasury_id=quote(str(treasury_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TreasuryStatementsPaginatedResponse | None:
    if response.status_code == 200:
        response_200 = TreasuryStatementsPaginatedResponse.from_dict(response.json())

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
) -> Response[Any | TreasuryStatementsPaginatedResponse]:
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
    limit: int | Unset = 1000,
    order: GetTreasuryStatementsOrder | Unset = GetTreasuryStatementsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    document_type: GetTreasuryStatementsDocumentType | Unset = UNSET,
) -> Response[Any | TreasuryStatementsPaginatedResponse]:
    """Get treasury account statements

     Retrieve a paginated list of statements for a specific treasury account. Supports cursor-based
    pagination and filtering by document type.

    Args:
        treasury_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (GetTreasuryStatementsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults
            to 'asc' Default: GetTreasuryStatementsOrder.ASC.
        start_after (UUID | Unset): The ID of the statement to start the page after (exclusive).
            When provided, results will begin with the statement immediately following this ID. Use
            this for standard forward pagination to get the next page of results. Cannot be combined
            with end_before.
        end_before (UUID | Unset): The ID of the statement to end the page before (exclusive).
            When provided, results will end just before this ID and work backwards. Use this for
            reverse pagination or to retrieve previous pages. Cannot be combined with start_after.
        document_type (GetTreasuryStatementsDocumentType | Unset): Filter statements by document
            type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TreasuryStatementsPaginatedResponse]
    """

    kwargs = _get_kwargs(
        treasury_id=treasury_id,
        limit=limit,
        order=order,
        start_after=start_after,
        end_before=end_before,
        document_type=document_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    treasury_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    order: GetTreasuryStatementsOrder | Unset = GetTreasuryStatementsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    document_type: GetTreasuryStatementsDocumentType | Unset = UNSET,
) -> Any | TreasuryStatementsPaginatedResponse | None:
    """Get treasury account statements

     Retrieve a paginated list of statements for a specific treasury account. Supports cursor-based
    pagination and filtering by document type.

    Args:
        treasury_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (GetTreasuryStatementsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults
            to 'asc' Default: GetTreasuryStatementsOrder.ASC.
        start_after (UUID | Unset): The ID of the statement to start the page after (exclusive).
            When provided, results will begin with the statement immediately following this ID. Use
            this for standard forward pagination to get the next page of results. Cannot be combined
            with end_before.
        end_before (UUID | Unset): The ID of the statement to end the page before (exclusive).
            When provided, results will end just before this ID and work backwards. Use this for
            reverse pagination or to retrieve previous pages. Cannot be combined with start_after.
        document_type (GetTreasuryStatementsDocumentType | Unset): Filter statements by document
            type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TreasuryStatementsPaginatedResponse
    """

    return sync_detailed(
        treasury_id=treasury_id,
        client=client,
        limit=limit,
        order=order,
        start_after=start_after,
        end_before=end_before,
        document_type=document_type,
    ).parsed


async def asyncio_detailed(
    treasury_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    order: GetTreasuryStatementsOrder | Unset = GetTreasuryStatementsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    document_type: GetTreasuryStatementsDocumentType | Unset = UNSET,
) -> Response[Any | TreasuryStatementsPaginatedResponse]:
    """Get treasury account statements

     Retrieve a paginated list of statements for a specific treasury account. Supports cursor-based
    pagination and filtering by document type.

    Args:
        treasury_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (GetTreasuryStatementsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults
            to 'asc' Default: GetTreasuryStatementsOrder.ASC.
        start_after (UUID | Unset): The ID of the statement to start the page after (exclusive).
            When provided, results will begin with the statement immediately following this ID. Use
            this for standard forward pagination to get the next page of results. Cannot be combined
            with end_before.
        end_before (UUID | Unset): The ID of the statement to end the page before (exclusive).
            When provided, results will end just before this ID and work backwards. Use this for
            reverse pagination or to retrieve previous pages. Cannot be combined with start_after.
        document_type (GetTreasuryStatementsDocumentType | Unset): Filter statements by document
            type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TreasuryStatementsPaginatedResponse]
    """

    kwargs = _get_kwargs(
        treasury_id=treasury_id,
        limit=limit,
        order=order,
        start_after=start_after,
        end_before=end_before,
        document_type=document_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    treasury_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    order: GetTreasuryStatementsOrder | Unset = GetTreasuryStatementsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    document_type: GetTreasuryStatementsDocumentType | Unset = UNSET,
) -> Any | TreasuryStatementsPaginatedResponse | None:
    """Get treasury account statements

     Retrieve a paginated list of statements for a specific treasury account. Supports cursor-based
    pagination and filtering by document type.

    Args:
        treasury_id (UUID): ID for a Mercury account.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        order (GetTreasuryStatementsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults
            to 'asc' Default: GetTreasuryStatementsOrder.ASC.
        start_after (UUID | Unset): The ID of the statement to start the page after (exclusive).
            When provided, results will begin with the statement immediately following this ID. Use
            this for standard forward pagination to get the next page of results. Cannot be combined
            with end_before.
        end_before (UUID | Unset): The ID of the statement to end the page before (exclusive).
            When provided, results will end just before this ID and work backwards. Use this for
            reverse pagination or to retrieve previous pages. Cannot be combined with start_after.
        document_type (GetTreasuryStatementsDocumentType | Unset): Filter statements by document
            type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TreasuryStatementsPaginatedResponse
    """

    return (
        await asyncio_detailed(
            treasury_id=treasury_id,
            client=client,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
            document_type=document_type,
        )
    ).parsed
