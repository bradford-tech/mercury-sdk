from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_send_money_approval_requests_status import ListSendMoneyApprovalRequestsStatus
from ...models.send_money_approval_requests_paginated_response import SendMoneyApprovalRequestsPaginatedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_id: UUID | Unset = UNSET,
    status: ListSendMoneyApprovalRequestsStatus | Unset = UNSET,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    limit: int | Unset = 1000,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_account_id: str | Unset = UNSET
    if not isinstance(account_id, Unset):
        json_account_id = str(account_id)
    params["accountId"] = json_account_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_start_after: str | Unset = UNSET
    if not isinstance(start_after, Unset):
        json_start_after = str(start_after)
    params["start_after"] = json_start_after

    json_end_before: str | Unset = UNSET
    if not isinstance(end_before, Unset):
        json_end_before = str(end_before)
    params["end_before"] = json_end_before

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/request-send-money",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SendMoneyApprovalRequestsPaginatedResponse | None:
    if response.status_code == 200:
        response_200 = SendMoneyApprovalRequestsPaginatedResponse.from_dict(response.json())

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
) -> Response[Any | SendMoneyApprovalRequestsPaginatedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID | Unset = UNSET,
    status: ListSendMoneyApprovalRequestsStatus | Unset = UNSET,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    limit: int | Unset = 1000,
) -> Response[Any | SendMoneyApprovalRequestsPaginatedResponse]:
    """List send money approval requests

     Retrieve a paginated list of send money approval requests for the authenticated organization.
    Supports filtering by account and status.

    Args:
        account_id (UUID | Unset): ID for a Mercury account.
        status (ListSendMoneyApprovalRequestsStatus | Unset):
        start_after (UUID | Unset): The ID of the send money approval request to start the page
            after (exclusive). When provided, results will begin with the send money approval request
            immediately following this ID. Use this for standard forward pagination to get the next
            page of results. Cannot be combined with end_before.
        end_before (UUID | Unset): The ID of the send money approval request to end the page
            before (exclusive). When provided, results will end just before this ID and work
            backwards. Use this for reverse pagination or to retrieve previous pages. Cannot be
            combined with start_after.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SendMoneyApprovalRequestsPaginatedResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        status=status,
        start_after=start_after,
        end_before=end_before,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID | Unset = UNSET,
    status: ListSendMoneyApprovalRequestsStatus | Unset = UNSET,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    limit: int | Unset = 1000,
) -> Any | SendMoneyApprovalRequestsPaginatedResponse | None:
    """List send money approval requests

     Retrieve a paginated list of send money approval requests for the authenticated organization.
    Supports filtering by account and status.

    Args:
        account_id (UUID | Unset): ID for a Mercury account.
        status (ListSendMoneyApprovalRequestsStatus | Unset):
        start_after (UUID | Unset): The ID of the send money approval request to start the page
            after (exclusive). When provided, results will begin with the send money approval request
            immediately following this ID. Use this for standard forward pagination to get the next
            page of results. Cannot be combined with end_before.
        end_before (UUID | Unset): The ID of the send money approval request to end the page
            before (exclusive). When provided, results will end just before this ID and work
            backwards. Use this for reverse pagination or to retrieve previous pages. Cannot be
            combined with start_after.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SendMoneyApprovalRequestsPaginatedResponse
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        status=status,
        start_after=start_after,
        end_before=end_before,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID | Unset = UNSET,
    status: ListSendMoneyApprovalRequestsStatus | Unset = UNSET,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    limit: int | Unset = 1000,
) -> Response[Any | SendMoneyApprovalRequestsPaginatedResponse]:
    """List send money approval requests

     Retrieve a paginated list of send money approval requests for the authenticated organization.
    Supports filtering by account and status.

    Args:
        account_id (UUID | Unset): ID for a Mercury account.
        status (ListSendMoneyApprovalRequestsStatus | Unset):
        start_after (UUID | Unset): The ID of the send money approval request to start the page
            after (exclusive). When provided, results will begin with the send money approval request
            immediately following this ID. Use this for standard forward pagination to get the next
            page of results. Cannot be combined with end_before.
        end_before (UUID | Unset): The ID of the send money approval request to end the page
            before (exclusive). When provided, results will end just before this ID and work
            backwards. Use this for reverse pagination or to retrieve previous pages. Cannot be
            combined with start_after.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SendMoneyApprovalRequestsPaginatedResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        status=status,
        start_after=start_after,
        end_before=end_before,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID | Unset = UNSET,
    status: ListSendMoneyApprovalRequestsStatus | Unset = UNSET,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    limit: int | Unset = 1000,
) -> Any | SendMoneyApprovalRequestsPaginatedResponse | None:
    """List send money approval requests

     Retrieve a paginated list of send money approval requests for the authenticated organization.
    Supports filtering by account and status.

    Args:
        account_id (UUID | Unset): ID for a Mercury account.
        status (ListSendMoneyApprovalRequestsStatus | Unset):
        start_after (UUID | Unset): The ID of the send money approval request to start the page
            after (exclusive). When provided, results will begin with the send money approval request
            immediately following this ID. Use this for standard forward pagination to get the next
            page of results. Cannot be combined with end_before.
        end_before (UUID | Unset): The ID of the send money approval request to end the page
            before (exclusive). When provided, results will end just before this ID and work
            backwards. Use this for reverse pagination or to retrieve previous pages. Cannot be
            combined with start_after.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SendMoneyApprovalRequestsPaginatedResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            status=status,
            start_after=start_after,
            end_before=end_before,
            limit=limit,
        )
    ).parsed
