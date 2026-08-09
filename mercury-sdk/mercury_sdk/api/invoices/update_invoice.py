from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_ar_invoice_response import ApiV1ArInvoiceResponse
from ...models.api_v1_ar_invoice_update_request import ApiV1ArInvoiceUpdateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    invoice_id: UUID,
    *,
    body: ApiV1ArInvoiceUpdateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ar/invoices/{invoice_id}".format(
            invoice_id=quote(str(invoice_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiV1ArInvoiceResponse | None:
    if response.status_code == 200:
        response_200 = ApiV1ArInvoiceResponse.from_dict(response.json())

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
) -> Response[Any | ApiV1ArInvoiceResponse]:
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
    body: ApiV1ArInvoiceUpdateRequest | Unset = UNSET,
) -> Response[Any | ApiV1ArInvoiceResponse]:
    """Update an invoice

     Update an existing invoice

    Args:
        invoice_id (UUID): ID for the invoice.
        body (ApiV1ArInvoiceUpdateRequest | Unset):  The request body to update an invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1ArInvoiceResponse]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ApiV1ArInvoiceUpdateRequest | Unset = UNSET,
) -> Any | ApiV1ArInvoiceResponse | None:
    """Update an invoice

     Update an existing invoice

    Args:
        invoice_id (UUID): ID for the invoice.
        body (ApiV1ArInvoiceUpdateRequest | Unset):  The request body to update an invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1ArInvoiceResponse
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    invoice_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ApiV1ArInvoiceUpdateRequest | Unset = UNSET,
) -> Response[Any | ApiV1ArInvoiceResponse]:
    """Update an invoice

     Update an existing invoice

    Args:
        invoice_id (UUID): ID for the invoice.
        body (ApiV1ArInvoiceUpdateRequest | Unset):  The request body to update an invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1ArInvoiceResponse]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ApiV1ArInvoiceUpdateRequest | Unset = UNSET,
) -> Any | ApiV1ArInvoiceResponse | None:
    """Update an invoice

     Update an existing invoice

    Args:
        invoice_id (UUID): ID for the invoice.
        body (ApiV1ArInvoiceUpdateRequest | Unset):  The request body to update an invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1ArInvoiceResponse
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
            body=body,
        )
    ).parsed
