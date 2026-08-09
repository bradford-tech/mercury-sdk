from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_events_paginated_response import ApiEventsPaginatedResponse
from ...models.get_events_order import GetEventsOrder
from ...models.get_events_resource_type import GetEventsResourceType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 1000,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    order: GetEventsOrder | Unset = GetEventsOrder.ASC,
    resource_type: GetEventsResourceType | Unset = UNSET,
    resource_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_start_after: str | Unset = UNSET
    if not isinstance(start_after, Unset):
        json_start_after = str(start_after)
    params["start_after"] = json_start_after

    json_end_before: str | Unset = UNSET
    if not isinstance(end_before, Unset):
        json_end_before = str(end_before)
    params["end_before"] = json_end_before

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    json_resource_type: str | Unset = UNSET
    if not isinstance(resource_type, Unset):
        json_resource_type = resource_type.value

    params["resourceType"] = json_resource_type

    json_resource_id: str | Unset = UNSET
    if not isinstance(resource_id, Unset):
        json_resource_id = str(resource_id)
    params["resourceId"] = json_resource_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiEventsPaginatedResponse | None:
    if response.status_code == 200:
        response_200 = ApiEventsPaginatedResponse.from_dict(response.json())

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
) -> Response[Any | ApiEventsPaginatedResponse]:
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
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    order: GetEventsOrder | Unset = GetEventsOrder.ASC,
    resource_type: GetEventsResourceType | Unset = UNSET,
    resource_id: UUID | Unset = UNSET,
) -> Response[Any | ApiEventsPaginatedResponse]:
    """Get all events

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start_after (UUID | Unset): The ID of the event to start the page after (exclusive). When
            provided, results will begin with the event immediately following this ID. Use this for
            standard forward pagination to get the next page of results. Cannot be combined with
            end_before.
        end_before (UUID | Unset): The ID of the event to end the page before (exclusive). When
            provided, results will end just before this ID and work backwards. Use this for reverse
            pagination or to retrieve previous pages. Cannot be combined with start_after.
        order (GetEventsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to 'asc'
            Default: GetEventsOrder.ASC.
        resource_type (GetEventsResourceType | Unset):
        resource_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiEventsPaginatedResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        start_after=start_after,
        end_before=end_before,
        order=order,
        resource_type=resource_type,
        resource_id=resource_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    order: GetEventsOrder | Unset = GetEventsOrder.ASC,
    resource_type: GetEventsResourceType | Unset = UNSET,
    resource_id: UUID | Unset = UNSET,
) -> Any | ApiEventsPaginatedResponse | None:
    """Get all events

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start_after (UUID | Unset): The ID of the event to start the page after (exclusive). When
            provided, results will begin with the event immediately following this ID. Use this for
            standard forward pagination to get the next page of results. Cannot be combined with
            end_before.
        end_before (UUID | Unset): The ID of the event to end the page before (exclusive). When
            provided, results will end just before this ID and work backwards. Use this for reverse
            pagination or to retrieve previous pages. Cannot be combined with start_after.
        order (GetEventsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to 'asc'
            Default: GetEventsOrder.ASC.
        resource_type (GetEventsResourceType | Unset):
        resource_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiEventsPaginatedResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        start_after=start_after,
        end_before=end_before,
        order=order,
        resource_type=resource_type,
        resource_id=resource_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    order: GetEventsOrder | Unset = GetEventsOrder.ASC,
    resource_type: GetEventsResourceType | Unset = UNSET,
    resource_id: UUID | Unset = UNSET,
) -> Response[Any | ApiEventsPaginatedResponse]:
    """Get all events

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start_after (UUID | Unset): The ID of the event to start the page after (exclusive). When
            provided, results will begin with the event immediately following this ID. Use this for
            standard forward pagination to get the next page of results. Cannot be combined with
            end_before.
        end_before (UUID | Unset): The ID of the event to end the page before (exclusive). When
            provided, results will end just before this ID and work backwards. Use this for reverse
            pagination or to retrieve previous pages. Cannot be combined with start_after.
        order (GetEventsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to 'asc'
            Default: GetEventsOrder.ASC.
        resource_type (GetEventsResourceType | Unset):
        resource_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiEventsPaginatedResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        start_after=start_after,
        end_before=end_before,
        order=order,
        resource_type=resource_type,
        resource_id=resource_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    order: GetEventsOrder | Unset = GetEventsOrder.ASC,
    resource_type: GetEventsResourceType | Unset = UNSET,
    resource_id: UUID | Unset = UNSET,
) -> Any | ApiEventsPaginatedResponse | None:
    """Get all events

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start_after (UUID | Unset): The ID of the event to start the page after (exclusive). When
            provided, results will begin with the event immediately following this ID. Use this for
            standard forward pagination to get the next page of results. Cannot be combined with
            end_before.
        end_before (UUID | Unset): The ID of the event to end the page before (exclusive). When
            provided, results will end just before this ID and work backwards. Use this for reverse
            pagination or to retrieve previous pages. Cannot be combined with start_after.
        order (GetEventsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to 'asc'
            Default: GetEventsOrder.ASC.
        resource_type (GetEventsResourceType | Unset):
        resource_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiEventsPaginatedResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
            resource_type=resource_type,
            resource_id=resource_id,
        )
    ).parsed
