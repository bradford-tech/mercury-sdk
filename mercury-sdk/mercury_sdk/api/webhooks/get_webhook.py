from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_webhook_response import ApiWebhookResponse
from ...types import Response


def _get_kwargs(
    webhook_endpoint_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhooks/{webhook_endpoint_id}".format(
            webhook_endpoint_id=quote(str(webhook_endpoint_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiWebhookResponse | None:
    if response.status_code == 200:
        response_200 = ApiWebhookResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ApiWebhookResponse]:
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
) -> Response[Any | ApiWebhookResponse]:
    """Get webhook endpoint by ID

     Retrieve details of a specific webhook endpoint by ID

    Args:
        webhook_endpoint_id (UUID): ID for the webhook

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiWebhookResponse]
    """

    kwargs = _get_kwargs(
        webhook_endpoint_id=webhook_endpoint_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_endpoint_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ApiWebhookResponse | None:
    """Get webhook endpoint by ID

     Retrieve details of a specific webhook endpoint by ID

    Args:
        webhook_endpoint_id (UUID): ID for the webhook

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiWebhookResponse
    """

    return sync_detailed(
        webhook_endpoint_id=webhook_endpoint_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    webhook_endpoint_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ApiWebhookResponse]:
    """Get webhook endpoint by ID

     Retrieve details of a specific webhook endpoint by ID

    Args:
        webhook_endpoint_id (UUID): ID for the webhook

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiWebhookResponse]
    """

    kwargs = _get_kwargs(
        webhook_endpoint_id=webhook_endpoint_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_endpoint_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ApiWebhookResponse | None:
    """Get webhook endpoint by ID

     Retrieve details of a specific webhook endpoint by ID

    Args:
        webhook_endpoint_id (UUID): ID for the webhook

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiWebhookResponse
    """

    return (
        await asyncio_detailed(
            webhook_endpoint_id=webhook_endpoint_id,
            client=client,
        )
    ).parsed
