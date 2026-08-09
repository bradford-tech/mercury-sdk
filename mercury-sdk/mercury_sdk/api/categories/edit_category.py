from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.category_data import CategoryData
from ...models.edit_category_api_request import EditCategoryApiRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    expense_category_id: UUID,
    *,
    body: EditCategoryApiRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/categories/{expense_category_id}".format(
            expense_category_id=quote(str(expense_category_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CategoryData | None:
    if response.status_code == 200:
        response_200 = CategoryData.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | CategoryData]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    expense_category_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: EditCategoryApiRequest | Unset = UNSET,
) -> Response[Any | CategoryData]:
    """Edit a category

     Update an existing custom expense category for the organization.

    Args:
        expense_category_id (UUID): ID for the category
        body (EditCategoryApiRequest | Unset):  Request body for editing an existing expense
            category. All fields are optional.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CategoryData]
    """

    kwargs = _get_kwargs(
        expense_category_id=expense_category_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    expense_category_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: EditCategoryApiRequest | Unset = UNSET,
) -> Any | CategoryData | None:
    """Edit a category

     Update an existing custom expense category for the organization.

    Args:
        expense_category_id (UUID): ID for the category
        body (EditCategoryApiRequest | Unset):  Request body for editing an existing expense
            category. All fields are optional.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CategoryData
    """

    return sync_detailed(
        expense_category_id=expense_category_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    expense_category_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: EditCategoryApiRequest | Unset = UNSET,
) -> Response[Any | CategoryData]:
    """Edit a category

     Update an existing custom expense category for the organization.

    Args:
        expense_category_id (UUID): ID for the category
        body (EditCategoryApiRequest | Unset):  Request body for editing an existing expense
            category. All fields are optional.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CategoryData]
    """

    kwargs = _get_kwargs(
        expense_category_id=expense_category_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    expense_category_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: EditCategoryApiRequest | Unset = UNSET,
) -> Any | CategoryData | None:
    """Edit a category

     Update an existing custom expense category for the organization.

    Args:
        expense_category_id (UUID): ID for the category
        body (EditCategoryApiRequest | Unset):  Request body for editing an existing expense
            category. All fields are optional.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CategoryData
    """

    return (
        await asyncio_detailed(
            expense_category_id=expense_category_id,
            client=client,
            body=body,
        )
    ).parsed
