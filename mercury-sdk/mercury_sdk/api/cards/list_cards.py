from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.card_list_response import CardListResponse
from ...models.list_cards_kind_item import ListCardsKindItem
from ...models.list_cards_order import ListCardsOrder
from ...models.list_cards_status_item import ListCardsStatusItem
from ...models.list_cards_type_item import ListCardsTypeItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_id: list[str] | Unset = UNSET,
    status: list[ListCardsStatusItem] | Unset = UNSET,
    type_: list[ListCardsTypeItem] | Unset = UNSET,
    kind: list[ListCardsKindItem] | Unset = UNSET,
    user_id: str | Unset = UNSET,
    limit: int | Unset = 500,
    order: ListCardsOrder | Unset = ListCardsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_account_id: list[str] | Unset = UNSET
    if not isinstance(account_id, Unset):
        json_account_id = account_id

    params["accountId"] = json_account_id

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item = type_item_data.value
            json_type_.append(type_item)

    params["type"] = json_type_

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = []
        for kind_item_data in kind:
            kind_item = kind_item_data.value
            json_kind.append(kind_item)

    params["kind"] = json_kind

    params["userId"] = user_id

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
        "url": "/cards",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CardListResponse | None:
    if response.status_code == 200:
        response_200 = CardListResponse.from_dict(response.json())

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
) -> Response[Any | CardListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: list[str] | Unset = UNSET,
    status: list[ListCardsStatusItem] | Unset = UNSET,
    type_: list[ListCardsTypeItem] | Unset = UNSET,
    kind: list[ListCardsKindItem] | Unset = UNSET,
    user_id: str | Unset = UNSET,
    limit: int | Unset = 500,
    order: ListCardsOrder | Unset = ListCardsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
) -> Response[Any | CardListResponse]:
    """List cards

     Retrieve a paginated list of cards.

    Args:
        account_id (list[str] | Unset): Filter cards by one or more account IDs.
        status (list[ListCardsStatusItem] | Unset): Filter cards by one or more statuses.
        type_ (list[ListCardsTypeItem] | Unset): Filter cards by type (virtual or physical).
        kind (list[ListCardsKindItem] | Unset): Filter cards by kind (debit or credit).
        user_id (str | Unset): Filter cards by the cardholder's user ID.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 500 Default: 500.
        order (ListCardsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to 'asc'
            Default: ListCardsOrder.ASC.
        start_after (UUID | Unset): The ID of the card to start the page after (exclusive). When
            provided, results will begin with the card immediately following this ID. Use this for
            standard forward pagination to get the next page of results. Cannot be combined with
            end_before.
        end_before (UUID | Unset): The ID of the card to end the page before (exclusive). When
            provided, results will end just before this ID and work backwards. Use this for reverse
            pagination or to retrieve previous pages. Cannot be combined with start_after.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CardListResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        status=status,
        type_=type_,
        kind=kind,
        user_id=user_id,
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
    account_id: list[str] | Unset = UNSET,
    status: list[ListCardsStatusItem] | Unset = UNSET,
    type_: list[ListCardsTypeItem] | Unset = UNSET,
    kind: list[ListCardsKindItem] | Unset = UNSET,
    user_id: str | Unset = UNSET,
    limit: int | Unset = 500,
    order: ListCardsOrder | Unset = ListCardsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
) -> Any | CardListResponse | None:
    """List cards

     Retrieve a paginated list of cards.

    Args:
        account_id (list[str] | Unset): Filter cards by one or more account IDs.
        status (list[ListCardsStatusItem] | Unset): Filter cards by one or more statuses.
        type_ (list[ListCardsTypeItem] | Unset): Filter cards by type (virtual or physical).
        kind (list[ListCardsKindItem] | Unset): Filter cards by kind (debit or credit).
        user_id (str | Unset): Filter cards by the cardholder's user ID.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 500 Default: 500.
        order (ListCardsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to 'asc'
            Default: ListCardsOrder.ASC.
        start_after (UUID | Unset): The ID of the card to start the page after (exclusive). When
            provided, results will begin with the card immediately following this ID. Use this for
            standard forward pagination to get the next page of results. Cannot be combined with
            end_before.
        end_before (UUID | Unset): The ID of the card to end the page before (exclusive). When
            provided, results will end just before this ID and work backwards. Use this for reverse
            pagination or to retrieve previous pages. Cannot be combined with start_after.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CardListResponse
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        status=status,
        type_=type_,
        kind=kind,
        user_id=user_id,
        limit=limit,
        order=order,
        start_after=start_after,
        end_before=end_before,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: list[str] | Unset = UNSET,
    status: list[ListCardsStatusItem] | Unset = UNSET,
    type_: list[ListCardsTypeItem] | Unset = UNSET,
    kind: list[ListCardsKindItem] | Unset = UNSET,
    user_id: str | Unset = UNSET,
    limit: int | Unset = 500,
    order: ListCardsOrder | Unset = ListCardsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
) -> Response[Any | CardListResponse]:
    """List cards

     Retrieve a paginated list of cards.

    Args:
        account_id (list[str] | Unset): Filter cards by one or more account IDs.
        status (list[ListCardsStatusItem] | Unset): Filter cards by one or more statuses.
        type_ (list[ListCardsTypeItem] | Unset): Filter cards by type (virtual or physical).
        kind (list[ListCardsKindItem] | Unset): Filter cards by kind (debit or credit).
        user_id (str | Unset): Filter cards by the cardholder's user ID.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 500 Default: 500.
        order (ListCardsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to 'asc'
            Default: ListCardsOrder.ASC.
        start_after (UUID | Unset): The ID of the card to start the page after (exclusive). When
            provided, results will begin with the card immediately following this ID. Use this for
            standard forward pagination to get the next page of results. Cannot be combined with
            end_before.
        end_before (UUID | Unset): The ID of the card to end the page before (exclusive). When
            provided, results will end just before this ID and work backwards. Use this for reverse
            pagination or to retrieve previous pages. Cannot be combined with start_after.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CardListResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        status=status,
        type_=type_,
        kind=kind,
        user_id=user_id,
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
    account_id: list[str] | Unset = UNSET,
    status: list[ListCardsStatusItem] | Unset = UNSET,
    type_: list[ListCardsTypeItem] | Unset = UNSET,
    kind: list[ListCardsKindItem] | Unset = UNSET,
    user_id: str | Unset = UNSET,
    limit: int | Unset = 500,
    order: ListCardsOrder | Unset = ListCardsOrder.ASC,
    start_after: UUID | Unset = UNSET,
    end_before: UUID | Unset = UNSET,
) -> Any | CardListResponse | None:
    """List cards

     Retrieve a paginated list of cards.

    Args:
        account_id (list[str] | Unset): Filter cards by one or more account IDs.
        status (list[ListCardsStatusItem] | Unset): Filter cards by one or more statuses.
        type_ (list[ListCardsTypeItem] | Unset): Filter cards by type (virtual or physical).
        kind (list[ListCardsKindItem] | Unset): Filter cards by kind (debit or credit).
        user_id (str | Unset): Filter cards by the cardholder's user ID.
        limit (int | Unset): Maximum number of results to return. Allowed range: 1 to 1000.
            Defaults to 500 Default: 500.
        order (ListCardsOrder | Unset): Sort order. Can be 'asc' or 'desc'. Defaults to 'asc'
            Default: ListCardsOrder.ASC.
        start_after (UUID | Unset): The ID of the card to start the page after (exclusive). When
            provided, results will begin with the card immediately following this ID. Use this for
            standard forward pagination to get the next page of results. Cannot be combined with
            end_before.
        end_before (UUID | Unset): The ID of the card to end the page before (exclusive). When
            provided, results will end just before this ID and work backwards. Use this for reverse
            pagination or to retrieve previous pages. Cannot be combined with start_after.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CardListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            status=status,
            type_=type_,
            kind=kind,
            user_id=user_id,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
        )
    ).parsed
