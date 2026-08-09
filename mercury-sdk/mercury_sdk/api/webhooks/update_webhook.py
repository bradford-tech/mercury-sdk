from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_webhook_response import ApiWebhookResponse
from ...models.update_webhook_params import UpdateWebhookParams
from ...types import UNSET, Response, Unset


def _get_kwargs(
    webhook_endpoint_id: UUID,
    *,
    body: UpdateWebhookParams | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhooks/{webhook_endpoint_id}".format(
            webhook_endpoint_id=quote(str(webhook_endpoint_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiWebhookResponse | None:
    if response.status_code == 200:
        response_200 = ApiWebhookResponse.from_dict(response.json())

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
    body: UpdateWebhookParams | Unset = UNSET,
) -> Response[Any | ApiWebhookResponse]:
    """Update an existing webhook endpoint

     Update the configuration of an existing webhook endpoint. A webhook that has been disabled due to
    consecutive delivery failures can be reactivated by setting its status to 'active'.

    Args:
        webhook_endpoint_id (UUID): ID for the webhook
        body (UpdateWebhookParams | Unset):  Request body for updating an existing webhook
            endpoint.
             All fields are optional - only provided fields will be updated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiWebhookResponse]
    """

    kwargs = _get_kwargs(
        webhook_endpoint_id=webhook_endpoint_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_endpoint_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWebhookParams | Unset = UNSET,
) -> Any | ApiWebhookResponse | None:
    """Update an existing webhook endpoint

     Update the configuration of an existing webhook endpoint. A webhook that has been disabled due to
    consecutive delivery failures can be reactivated by setting its status to 'active'.

    Args:
        webhook_endpoint_id (UUID): ID for the webhook
        body (UpdateWebhookParams | Unset):  Request body for updating an existing webhook
            endpoint.
             All fields are optional - only provided fields will be updated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiWebhookResponse
    """

    return sync_detailed(
        webhook_endpoint_id=webhook_endpoint_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    webhook_endpoint_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWebhookParams | Unset = UNSET,
) -> Response[Any | ApiWebhookResponse]:
    """Update an existing webhook endpoint

     Update the configuration of an existing webhook endpoint. A webhook that has been disabled due to
    consecutive delivery failures can be reactivated by setting its status to 'active'.

    Args:
        webhook_endpoint_id (UUID): ID for the webhook
        body (UpdateWebhookParams | Unset):  Request body for updating an existing webhook
            endpoint.
             All fields are optional - only provided fields will be updated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiWebhookResponse]
    """

    kwargs = _get_kwargs(
        webhook_endpoint_id=webhook_endpoint_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_endpoint_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWebhookParams | Unset = UNSET,
) -> Any | ApiWebhookResponse | None:
    """Update an existing webhook endpoint

     Update the configuration of an existing webhook endpoint. A webhook that has been disabled due to
    consecutive delivery failures can be reactivated by setting its status to 'active'.

    Args:
        webhook_endpoint_id (UUID): ID for the webhook
        body (UpdateWebhookParams | Unset):  Request body for updating an existing webhook
            endpoint.
             All fields are optional - only provided fields will be updated.

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
            body=body,
        )
    ).parsed
