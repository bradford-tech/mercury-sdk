from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_ar_attachments_response_data import ApiV1ArAttachmentsResponseData
from ...types import Response


def _get_kwargs(
    invoice_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ar/invoices/{invoice_id}/attachments".format(
            invoice_id=quote(str(invoice_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiV1ArAttachmentsResponseData | None:
    if response.status_code == 200:
        response_200 = ApiV1ArAttachmentsResponseData.from_dict(response.json())

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
) -> Response[Any | ApiV1ArAttachmentsResponseData]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invoice_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ApiV1ArAttachmentsResponseData]:
    """List invoice attachments

     Retrieve a list of all attachments for a specific invoice

    Args:
        invoice_id (UUID): ID for the invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1ArAttachmentsResponseData]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ApiV1ArAttachmentsResponseData | None:
    """List invoice attachments

     Retrieve a list of all attachments for a specific invoice

    Args:
        invoice_id (UUID): ID for the invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1ArAttachmentsResponseData
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invoice_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ApiV1ArAttachmentsResponseData]:
    """List invoice attachments

     Retrieve a list of all attachments for a specific invoice

    Args:
        invoice_id (UUID): ID for the invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1ArAttachmentsResponseData]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ApiV1ArAttachmentsResponseData | None:
    """List invoice attachments

     Retrieve a list of all attachments for a specific invoice

    Args:
        invoice_id (UUID): ID for the invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1ArAttachmentsResponseData
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
        )
    ).parsed
