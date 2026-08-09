from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.card import Card
from ...models.update_card_request import UpdateCardRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    card_id: UUID,
    *,
    body: UpdateCardRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cards/{card_id}".format(
            card_id=quote(str(card_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Card | None:
    if response.status_code == 200:
        response_200 = Card.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Card]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    card_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCardRequest | Unset = UNSET,
) -> Response[Any | Card]:
    """Update a card

     Update a card's nickname or spending limits.

    Args:
        card_id (UUID): Unique identifier for a card
        body (UpdateCardRequest | Unset):  At least one updateable field must be provided;
             requests where every field is the same are rejected.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Card]
    """

    kwargs = _get_kwargs(
        card_id=card_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    card_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCardRequest | Unset = UNSET,
) -> Any | Card | None:
    """Update a card

     Update a card's nickname or spending limits.

    Args:
        card_id (UUID): Unique identifier for a card
        body (UpdateCardRequest | Unset):  At least one updateable field must be provided;
             requests where every field is the same are rejected.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Card
    """

    return sync_detailed(
        card_id=card_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    card_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCardRequest | Unset = UNSET,
) -> Response[Any | Card]:
    """Update a card

     Update a card's nickname or spending limits.

    Args:
        card_id (UUID): Unique identifier for a card
        body (UpdateCardRequest | Unset):  At least one updateable field must be provided;
             requests where every field is the same are rejected.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Card]
    """

    kwargs = _get_kwargs(
        card_id=card_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    card_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCardRequest | Unset = UNSET,
) -> Any | Card | None:
    """Update a card

     Update a card's nickname or spending limits.

    Args:
        card_id (UUID): Unique identifier for a card
        body (UpdateCardRequest | Unset):  At least one updateable field must be provided;
             requests where every field is the same are rejected.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Card
    """

    return (
        await asyncio_detailed(
            card_id=card_id,
            client=client,
            body=body,
        )
    ).parsed
