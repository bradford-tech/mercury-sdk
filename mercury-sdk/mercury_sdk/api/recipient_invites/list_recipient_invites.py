from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_recipient_invites_order import ListRecipientInvitesOrder
from ...models.list_recipient_invites_status import ListRecipientInvitesStatus
from ...models.recipient_invite_api_paginated_response import RecipientInviteApiPaginatedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 1000,
    start_after: str | Unset = UNSET,
    end_before: str | Unset = UNSET,
    order: ListRecipientInvitesOrder | Unset = ListRecipientInvitesOrder.ASC,
    status: ListRecipientInvitesStatus | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["start_after"] = start_after

    params["end_before"] = end_before

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/recipients/invites",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RecipientInviteApiPaginatedResponse | None:
    if response.status_code == 200:
        response_200 = RecipientInviteApiPaginatedResponse.from_dict(response.json())

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
) -> Response[Any | RecipientInviteApiPaginatedResponse]:
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
    start_after: str | Unset = UNSET,
    end_before: str | Unset = UNSET,
    order: ListRecipientInvitesOrder | Unset = ListRecipientInvitesOrder.ASC,
    status: ListRecipientInvitesStatus | Unset = UNSET,
) -> Response[Any | RecipientInviteApiPaginatedResponse]:
    """List recipient invites

     Retrieve a paginated list of all recipient invites for your organization. Supports filtering by
    status.

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start_after (str | Unset): The ID of the recipient invite to start the page after
            (exclusive). When provided, results will begin with the recipient invite immediately
            following this ID. Use this for standard forward pagination to get the next page of
            results. Cannot be combined with end_before.
        end_before (str | Unset): The ID of the recipient invite to end the page before
            (exclusive). When provided, results will end just before this ID and work backwards. Use
            this for reverse pagination or to retrieve previous pages. Cannot be combined with
            start_after.
        order (ListRecipientInvitesOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to
            'asc' Default: ListRecipientInvitesOrder.ASC.
        status (ListRecipientInvitesStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RecipientInviteApiPaginatedResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        start_after=start_after,
        end_before=end_before,
        order=order,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    start_after: str | Unset = UNSET,
    end_before: str | Unset = UNSET,
    order: ListRecipientInvitesOrder | Unset = ListRecipientInvitesOrder.ASC,
    status: ListRecipientInvitesStatus | Unset = UNSET,
) -> Any | RecipientInviteApiPaginatedResponse | None:
    """List recipient invites

     Retrieve a paginated list of all recipient invites for your organization. Supports filtering by
    status.

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start_after (str | Unset): The ID of the recipient invite to start the page after
            (exclusive). When provided, results will begin with the recipient invite immediately
            following this ID. Use this for standard forward pagination to get the next page of
            results. Cannot be combined with end_before.
        end_before (str | Unset): The ID of the recipient invite to end the page before
            (exclusive). When provided, results will end just before this ID and work backwards. Use
            this for reverse pagination or to retrieve previous pages. Cannot be combined with
            start_after.
        order (ListRecipientInvitesOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to
            'asc' Default: ListRecipientInvitesOrder.ASC.
        status (ListRecipientInvitesStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RecipientInviteApiPaginatedResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        start_after=start_after,
        end_before=end_before,
        order=order,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    start_after: str | Unset = UNSET,
    end_before: str | Unset = UNSET,
    order: ListRecipientInvitesOrder | Unset = ListRecipientInvitesOrder.ASC,
    status: ListRecipientInvitesStatus | Unset = UNSET,
) -> Response[Any | RecipientInviteApiPaginatedResponse]:
    """List recipient invites

     Retrieve a paginated list of all recipient invites for your organization. Supports filtering by
    status.

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start_after (str | Unset): The ID of the recipient invite to start the page after
            (exclusive). When provided, results will begin with the recipient invite immediately
            following this ID. Use this for standard forward pagination to get the next page of
            results. Cannot be combined with end_before.
        end_before (str | Unset): The ID of the recipient invite to end the page before
            (exclusive). When provided, results will end just before this ID and work backwards. Use
            this for reverse pagination or to retrieve previous pages. Cannot be combined with
            start_after.
        order (ListRecipientInvitesOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to
            'asc' Default: ListRecipientInvitesOrder.ASC.
        status (ListRecipientInvitesStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RecipientInviteApiPaginatedResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        start_after=start_after,
        end_before=end_before,
        order=order,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    start_after: str | Unset = UNSET,
    end_before: str | Unset = UNSET,
    order: ListRecipientInvitesOrder | Unset = ListRecipientInvitesOrder.ASC,
    status: ListRecipientInvitesStatus | Unset = UNSET,
) -> Any | RecipientInviteApiPaginatedResponse | None:
    """List recipient invites

     Retrieve a paginated list of all recipient invites for your organization. Supports filtering by
    status.

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start_after (str | Unset): The ID of the recipient invite to start the page after
            (exclusive). When provided, results will begin with the recipient invite immediately
            following this ID. Use this for standard forward pagination to get the next page of
            results. Cannot be combined with end_before.
        end_before (str | Unset): The ID of the recipient invite to end the page before
            (exclusive). When provided, results will end just before this ID and work backwards. Use
            this for reverse pagination or to retrieve previous pages. Cannot be combined with
            start_after.
        order (ListRecipientInvitesOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to
            'asc' Default: ListRecipientInvitesOrder.ASC.
        status (ListRecipientInvitesStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RecipientInviteApiPaginatedResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
            status=status,
        )
    ).parsed
