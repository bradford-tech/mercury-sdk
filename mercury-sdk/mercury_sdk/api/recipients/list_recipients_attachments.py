from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_recipients_attachments_order import ListRecipientsAttachmentsOrder
from ...models.recipients_attachments_paginated_response import RecipientsAttachmentsPaginatedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 1000,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    order: ListRecipientsAttachmentsOrder | Unset = ListRecipientsAttachmentsOrder.ASC,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/recipients/attachments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RecipientsAttachmentsPaginatedResponse | None:
    if response.status_code == 200:
        response_200 = RecipientsAttachmentsPaginatedResponse.from_dict(response.json())

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
) -> Response[Any | RecipientsAttachmentsPaginatedResponse]:
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
    order: ListRecipientsAttachmentsOrder | Unset = ListRecipientsAttachmentsOrder.ASC,
) -> Response[Any | RecipientsAttachmentsPaginatedResponse]:
    """List all recipient attachments

     Retrieve a paginated list of all recipient tax form attachments across all recipients in the
    organization. Use cursor parameters (start_after, end_before) for pagination.

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start_after (UUID | Unset): The ID of the recipient attachment to start the page after
            (exclusive). When provided, results will begin with the recipient attachment immediately
            following this ID. Use this for standard forward pagination to get the next page of
            results. Cannot be combined with end_before.
        end_before (UUID | Unset): The ID of the recipient attachment to end the page before
            (exclusive). When provided, results will end just before this ID and work backwards. Use
            this for reverse pagination or to retrieve previous pages. Cannot be combined with
            start_after.
        order (ListRecipientsAttachmentsOrder | Unset): Sort order. Can be 'asc' or 'desc'.
            Defaults to 'asc' Default: ListRecipientsAttachmentsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RecipientsAttachmentsPaginatedResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        start_after=start_after,
        end_before=end_before,
        order=order,
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
    order: ListRecipientsAttachmentsOrder | Unset = ListRecipientsAttachmentsOrder.ASC,
) -> Any | RecipientsAttachmentsPaginatedResponse | None:
    """List all recipient attachments

     Retrieve a paginated list of all recipient tax form attachments across all recipients in the
    organization. Use cursor parameters (start_after, end_before) for pagination.

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start_after (UUID | Unset): The ID of the recipient attachment to start the page after
            (exclusive). When provided, results will begin with the recipient attachment immediately
            following this ID. Use this for standard forward pagination to get the next page of
            results. Cannot be combined with end_before.
        end_before (UUID | Unset): The ID of the recipient attachment to end the page before
            (exclusive). When provided, results will end just before this ID and work backwards. Use
            this for reverse pagination or to retrieve previous pages. Cannot be combined with
            start_after.
        order (ListRecipientsAttachmentsOrder | Unset): Sort order. Can be 'asc' or 'desc'.
            Defaults to 'asc' Default: ListRecipientsAttachmentsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RecipientsAttachmentsPaginatedResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        start_after=start_after,
        end_before=end_before,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    order: ListRecipientsAttachmentsOrder | Unset = ListRecipientsAttachmentsOrder.ASC,
) -> Response[Any | RecipientsAttachmentsPaginatedResponse]:
    """List all recipient attachments

     Retrieve a paginated list of all recipient tax form attachments across all recipients in the
    organization. Use cursor parameters (start_after, end_before) for pagination.

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start_after (UUID | Unset): The ID of the recipient attachment to start the page after
            (exclusive). When provided, results will begin with the recipient attachment immediately
            following this ID. Use this for standard forward pagination to get the next page of
            results. Cannot be combined with end_before.
        end_before (UUID | Unset): The ID of the recipient attachment to end the page before
            (exclusive). When provided, results will end just before this ID and work backwards. Use
            this for reverse pagination or to retrieve previous pages. Cannot be combined with
            start_after.
        order (ListRecipientsAttachmentsOrder | Unset): Sort order. Can be 'asc' or 'desc'.
            Defaults to 'asc' Default: ListRecipientsAttachmentsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RecipientsAttachmentsPaginatedResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        start_after=start_after,
        end_before=end_before,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 1000,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
    order: ListRecipientsAttachmentsOrder | Unset = ListRecipientsAttachmentsOrder.ASC,
) -> Any | RecipientsAttachmentsPaginatedResponse | None:
    """List all recipient attachments

     Retrieve a paginated list of all recipient tax form attachments across all recipients in the
    organization. Use cursor parameters (start_after, end_before) for pagination.

    Args:
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 1000 Default: 1000.
        start_after (UUID | Unset): The ID of the recipient attachment to start the page after
            (exclusive). When provided, results will begin with the recipient attachment immediately
            following this ID. Use this for standard forward pagination to get the next page of
            results. Cannot be combined with end_before.
        end_before (UUID | Unset): The ID of the recipient attachment to end the page before
            (exclusive). When provided, results will end just before this ID and work backwards. Use
            this for reverse pagination or to retrieve previous pages. Cannot be combined with
            start_after.
        order (ListRecipientsAttachmentsOrder | Unset): Sort order. Can be 'asc' or 'desc'.
            Defaults to 'asc' Default: ListRecipientsAttachmentsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RecipientsAttachmentsPaginatedResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )
    ).parsed
