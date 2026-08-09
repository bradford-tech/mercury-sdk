from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.send_money_api_request import SendMoneyAPIRequest
from ...models.send_money_approval_request_response import SendMoneyApprovalRequestResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: UUID,
    *,
    body: SendMoneyAPIRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/{account_id}/request-send-money".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SendMoneyApprovalRequestResponse | None:
    if response.status_code == 200:
        response_200 = SendMoneyApprovalRequestResponse.from_dict(response.json())

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
) -> Response[Any | SendMoneyApprovalRequestResponse]:
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
    body: SendMoneyAPIRequest | Unset = UNSET,
) -> Response[Any | SendMoneyApprovalRequestResponse]:
    r"""Request to send money

     Create a \"request to send money\" that will require approval based on your organization's approval
    policies.

    Args:
        account_id (UUID): ID for a Mercury account.
        body (SendMoneyAPIRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SendMoneyApprovalRequestResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SendMoneyAPIRequest | Unset = UNSET,
) -> Any | SendMoneyApprovalRequestResponse | None:
    r"""Request to send money

     Create a \"request to send money\" that will require approval based on your organization's approval
    policies.

    Args:
        account_id (UUID): ID for a Mercury account.
        body (SendMoneyAPIRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SendMoneyApprovalRequestResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SendMoneyAPIRequest | Unset = UNSET,
) -> Response[Any | SendMoneyApprovalRequestResponse]:
    r"""Request to send money

     Create a \"request to send money\" that will require approval based on your organization's approval
    policies.

    Args:
        account_id (UUID): ID for a Mercury account.
        body (SendMoneyAPIRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SendMoneyApprovalRequestResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SendMoneyAPIRequest | Unset = UNSET,
) -> Any | SendMoneyApprovalRequestResponse | None:
    r"""Request to send money

     Create a \"request to send money\" that will require approval based on your organization's approval
    policies.

    Args:
        account_id (UUID): ID for a Mercury account.
        body (SendMoneyAPIRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SendMoneyApprovalRequestResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
