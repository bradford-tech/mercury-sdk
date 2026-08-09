from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_recipient_attachment_body import UploadRecipientAttachmentBody
from ...types import Response


def _get_kwargs(
    recipient_id: UUID,
    *,
    body: UploadRecipientAttachmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/recipient/{recipient_id}/attachments".format(
            recipient_id=quote(str(recipient_id), safe=""),
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
    recipient_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UploadRecipientAttachmentBody,
) -> Response[Any]:
    """Upload a recipient attachment

     Upload a tax form attachment for a recipient. The file is uploaded via multipart/form-data.
    Supported file types include PDF, images (PNG, JPG, GIF), and common document formats. The
    attachment will be associated as a tax document for the recipient.

    Args:
        recipient_id (UUID):
        body (UploadRecipientAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        recipient_id=recipient_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    recipient_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UploadRecipientAttachmentBody,
) -> Response[Any]:
    """Upload a recipient attachment

     Upload a tax form attachment for a recipient. The file is uploaded via multipart/form-data.
    Supported file types include PDF, images (PNG, JPG, GIF), and common document formats. The
    attachment will be associated as a tax document for the recipient.

    Args:
        recipient_id (UUID):
        body (UploadRecipientAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        recipient_id=recipient_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
