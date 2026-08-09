from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.verify_webhook_params import VerifyWebhookParams
from ...types import UNSET, Response, Unset


def _get_kwargs(
    webhook_endpoint_id: UUID,
    *,
    body: VerifyWebhookParams | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhooks/{webhook_endpoint_id}/verify".format(
            webhook_endpoint_id=quote(str(webhook_endpoint_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook_endpoint_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: VerifyWebhookParams | Unset = UNSET,
) -> Response[Any]:
    """Verify a webhook endpoint

     Send a test event to verify the webhook endpoint is properly configured and reachable. The request
    body accepts an optional 'eventType' field to specify which event type to test (e.g.,
    'transaction.created', 'transaction.updated'). If omitted from the request body, defaults to
    'transaction.created'.

    Args:
        webhook_endpoint_id (UUID): ID for the webhook
        body (VerifyWebhookParams | Unset):  Request body for verifying a webhook endpoint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        webhook_endpoint_id=webhook_endpoint_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    webhook_endpoint_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: VerifyWebhookParams | Unset = UNSET,
) -> Response[Any]:
    """Verify a webhook endpoint

     Send a test event to verify the webhook endpoint is properly configured and reachable. The request
    body accepts an optional 'eventType' field to specify which event type to test (e.g.,
    'transaction.created', 'transaction.updated'). If omitted from the request body, defaults to
    'transaction.created'.

    Args:
        webhook_endpoint_id (UUID): ID for the webhook
        body (VerifyWebhookParams | Unset):  Request body for verifying a webhook endpoint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        webhook_endpoint_id=webhook_endpoint_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
