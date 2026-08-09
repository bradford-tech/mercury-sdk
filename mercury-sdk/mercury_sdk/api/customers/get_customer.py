from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_ar_customer_response_data import ApiV1ArCustomerResponseData
from ...types import Response


def _get_kwargs(
    customer_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ar/customers/{customer_id}".format(
            customer_id=quote(str(customer_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiV1ArCustomerResponseData | None:
    if response.status_code == 200:
        response_200 = ApiV1ArCustomerResponseData.from_dict(response.json())

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
) -> Response[Any | ApiV1ArCustomerResponseData]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ApiV1ArCustomerResponseData]:
    """Get a customer

     Retrieve details of a specific customer by their ID

    Args:
        customer_id (UUID): The customer who will receive the invoice. Use the
            /api/v1/ar/customers endpoint to list your customers and find the corresponding id, or
            create a new customer first.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1ArCustomerResponseData]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ApiV1ArCustomerResponseData | None:
    """Get a customer

     Retrieve details of a specific customer by their ID

    Args:
        customer_id (UUID): The customer who will receive the invoice. Use the
            /api/v1/ar/customers endpoint to list your customers and find the corresponding id, or
            create a new customer first.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1ArCustomerResponseData
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    customer_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ApiV1ArCustomerResponseData]:
    """Get a customer

     Retrieve details of a specific customer by their ID

    Args:
        customer_id (UUID): The customer who will receive the invoice. Use the
            /api/v1/ar/customers endpoint to list your customers and find the corresponding id, or
            create a new customer first.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1ArCustomerResponseData]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ApiV1ArCustomerResponseData | None:
    """Get a customer

     Retrieve details of a specific customer by their ID

    Args:
        customer_id (UUID): The customer who will receive the invoice. Use the
            /api/v1/ar/customers endpoint to list your customers and find the corresponding id, or
            create a new customer first.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1ArCustomerResponseData
    """

    return (
        await asyncio_detailed(
            customer_id=customer_id,
            client=client,
        )
    ).parsed
