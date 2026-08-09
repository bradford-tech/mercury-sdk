from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_ar_customer_response_data import ApiV1ArCustomerResponseData
from ...models.api_v1_ar_customer_update_request import ApiV1ArCustomerUpdateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    customer_id: UUID,
    *,
    body: ApiV1ArCustomerUpdateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ar/customers/{customer_id}".format(
            customer_id=quote(str(customer_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiV1ArCustomerResponseData | None:
    if response.status_code == 200:
        response_200 = ApiV1ArCustomerResponseData.from_dict(response.json())

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
    body: ApiV1ArCustomerUpdateRequest | Unset = UNSET,
) -> Response[Any | ApiV1ArCustomerResponseData]:
    """Update a customer

     Update an existing customer

    Args:
        customer_id (UUID): The customer who will receive the invoice. Use the
            /api/v1/ar/customers endpoint to list your customers and find the corresponding id, or
            create a new customer first.
        body (ApiV1ArCustomerUpdateRequest | Unset):  Request data to update a customer using the
            public api

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1ArCustomerResponseData]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ApiV1ArCustomerUpdateRequest | Unset = UNSET,
) -> Any | ApiV1ArCustomerResponseData | None:
    """Update a customer

     Update an existing customer

    Args:
        customer_id (UUID): The customer who will receive the invoice. Use the
            /api/v1/ar/customers endpoint to list your customers and find the corresponding id, or
            create a new customer first.
        body (ApiV1ArCustomerUpdateRequest | Unset):  Request data to update a customer using the
            public api

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1ArCustomerResponseData
    """

    return sync_detailed(
        customer_id=customer_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    customer_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ApiV1ArCustomerUpdateRequest | Unset = UNSET,
) -> Response[Any | ApiV1ArCustomerResponseData]:
    """Update a customer

     Update an existing customer

    Args:
        customer_id (UUID): The customer who will receive the invoice. Use the
            /api/v1/ar/customers endpoint to list your customers and find the corresponding id, or
            create a new customer first.
        body (ApiV1ArCustomerUpdateRequest | Unset):  Request data to update a customer using the
            public api

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1ArCustomerResponseData]
    """

    kwargs = _get_kwargs(
        customer_id=customer_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ApiV1ArCustomerUpdateRequest | Unset = UNSET,
) -> Any | ApiV1ArCustomerResponseData | None:
    """Update a customer

     Update an existing customer

    Args:
        customer_id (UUID): The customer who will receive the invoice. Use the
            /api/v1/ar/customers endpoint to list your customers and find the corresponding id, or
            create a new customer first.
        body (ApiV1ArCustomerUpdateRequest | Unset):  Request data to update a customer using the
            public api

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
            body=body,
        )
    ).parsed
