from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_ar_invoice_create_request import ApiV1ArInvoiceCreateRequest
from ...models.api_v1_ar_invoice_response import ApiV1ArInvoiceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ApiV1ArInvoiceCreateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ar/invoices",
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
    *,
    client: AuthenticatedClient | Client,
    body: ApiV1ArInvoiceCreateRequest | Unset = UNSET,
) -> Response[Any | ApiV1ArInvoiceResponse]:
    """Create an invoice

     Create a new invoice for the organization

    Args:
        body (ApiV1ArInvoiceCreateRequest | Unset):  The request body to create an invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1ArInvoiceResponse]
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
    body: ApiV1ArInvoiceCreateRequest | Unset = UNSET,
) -> Any | ApiV1ArInvoiceResponse | None:
    """Create an invoice

     Create a new invoice for the organization

    Args:
        body (ApiV1ArInvoiceCreateRequest | Unset):  The request body to create an invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1ArInvoiceResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ApiV1ArInvoiceCreateRequest | Unset = UNSET,
) -> Response[Any | ApiV1ArInvoiceResponse]:
    """Create an invoice

     Create a new invoice for the organization

    Args:
        body (ApiV1ArInvoiceCreateRequest | Unset):  The request body to create an invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1ArInvoiceResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ApiV1ArInvoiceCreateRequest | Unset = UNSET,
) -> Any | ApiV1ArInvoiceResponse | None:
    """Create an invoice

     Create a new invoice for the organization

    Args:
        body (ApiV1ArInvoiceCreateRequest | Unset):  The request body to create an invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1ArInvoiceResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
