from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_transaction_attachment_body import UploadTransactionAttachmentBody
from ...types import Response


def _get_kwargs(
    transaction_id: UUID,
    *,
    body: UploadTransactionAttachmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/transaction/{transaction_id}/attachments".format(
            transaction_id=quote(str(transaction_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 404:
        return None

    if response.status_code == 413:
        return None

    if response.status_code == 415:
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
    transaction_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UploadTransactionAttachmentBody,
) -> Response[Any]:
    """Upload a transaction attachment

     Upload a file attachment to a transaction. The file is uploaded via multipart/form-data. Supported
    file types include PDF, images (PNG, JPG, GIF), and common document formats.

    Args:
        transaction_id (UUID):
        body (UploadTransactionAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    transaction_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UploadTransactionAttachmentBody,
) -> Response[Any]:
    """Upload a transaction attachment

     Upload a file attachment to a transaction. The file is uploaded via multipart/form-data. Supported
    file types include PDF, images (PNG, JPG, GIF), and common document formats.

    Args:
        transaction_id (UUID):
        body (UploadTransactionAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
