from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.category_data import CategoryData
from ...models.create_category_api_request import CreateCategoryApiRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateCategoryApiRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/categories",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CategoryData | None:
    if response.status_code == 201:
        response_201 = CategoryData.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | CategoryData]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCategoryApiRequest | Unset = UNSET,
) -> Response[Any | CategoryData]:
    """Create a new category

     Create a new custom expense category for the organization.

    Args:
        body (CreateCategoryApiRequest | Unset):  Request body for creating a new expense category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CategoryData]
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
    body: CreateCategoryApiRequest | Unset = UNSET,
) -> Any | CategoryData | None:
    """Create a new category

     Create a new custom expense category for the organization.

    Args:
        body (CreateCategoryApiRequest | Unset):  Request body for creating a new expense category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CategoryData
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCategoryApiRequest | Unset = UNSET,
) -> Response[Any | CategoryData]:
    """Create a new category

     Create a new custom expense category for the organization.

    Args:
        body (CreateCategoryApiRequest | Unset):  Request body for creating a new expense category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CategoryData]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCategoryApiRequest | Unset = UNSET,
) -> Any | CategoryData | None:
    """Create a new category

     Create a new custom expense category for the organization.

    Args:
        body (CreateCategoryApiRequest | Unset):  Request body for creating a new expense category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CategoryData
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
