from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_recipient_invite_api_request import CreateRecipientInviteApiRequest
from ...models.recipient_invite_api_response import RecipientInviteApiResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateRecipientInviteApiRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/recipients/invites",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RecipientInviteApiResponse | None:
    if response.status_code == 201:
        response_201 = RecipientInviteApiResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RecipientInviteApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateRecipientInviteApiRequest | Unset = UNSET,
) -> Response[Any | RecipientInviteApiResponse]:
    """Create a recipient invite

     Create an invite for a recipient to submit their payment details. Supply a recipientId to invite an
    existing recipient; omit it to invite someone new, in which case the recipient is created when the
    invitee completes onboarding.

    Args:
        body (CreateRecipientInviteApiRequest | Unset):  Request body for creating a recipient
            invite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RecipientInviteApiResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateRecipientInviteApiRequest | Unset = UNSET,
) -> Any | RecipientInviteApiResponse | None:
    """Create a recipient invite

     Create an invite for a recipient to submit their payment details. Supply a recipientId to invite an
    existing recipient; omit it to invite someone new, in which case the recipient is created when the
    invitee completes onboarding.

    Args:
        body (CreateRecipientInviteApiRequest | Unset):  Request body for creating a recipient
            invite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RecipientInviteApiResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateRecipientInviteApiRequest | Unset = UNSET,
) -> Response[Any | RecipientInviteApiResponse]:
    """Create a recipient invite

     Create an invite for a recipient to submit their payment details. Supply a recipientId to invite an
    existing recipient; omit it to invite someone new, in which case the recipient is created when the
    invitee completes onboarding.

    Args:
        body (CreateRecipientInviteApiRequest | Unset):  Request body for creating a recipient
            invite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RecipientInviteApiResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateRecipientInviteApiRequest | Unset = UNSET,
) -> Any | RecipientInviteApiResponse | None:
    """Create a recipient invite

     Create an invite for a recipient to submit their payment details. Supply a recipientId to invite an
    existing recipient; omit it to invite someone new, in which case the recipient is created when the
    invitee completes onboarding.

    Args:
        body (CreateRecipientInviteApiRequest | Unset):  Request body for creating a recipient
            invite.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RecipientInviteApiResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
