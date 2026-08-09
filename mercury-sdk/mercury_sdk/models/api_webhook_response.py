from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_webhook_status import ApiWebhookStatus
from ..models.resource_field import ResourceField
from ..models.webhook_event_type import WebhookEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiWebhookResponse")


@_attrs_define
class ApiWebhookResponse:
    """Webhook configuration details

    Attributes:
        created_at (datetime.datetime):  When the webhook was created Example: 2016-07-22T00:00:00Z.
        id (UUID):  Unique identifier for the webhook endpoint
        status (ApiWebhookStatus): The status of the webhook endpoint. 'active': delivering events normally. 'paused':
            paused by the user. 'disabled': automatically disabled by the system due to consecutive delivery failures. A
            disabled webhook can be reactivated by updating its status to 'active'.
        updated_at (datetime.datetime):  When the webhook was last updated Example: 2016-07-22T00:00:00Z.
        url (str):  The URL that will receive webhook POST requests
        event_types (list[WebhookEventType] | None | Unset):  Optional array of event types this webhook is subscribed
            to. Nothing means all events.
        filter_paths (list[ResourceField] | None | Unset):  Optional array of resource field paths to filter events by.
            Nothing means no filtering.
        secret (None | str | Unset):  Webhook signing secret. Only returned on creation (POST), not on GET or UPDATE
            operations.
    """

    created_at: datetime.datetime
    id: UUID
    status: ApiWebhookStatus
    updated_at: datetime.datetime
    url: str
    event_types: list[WebhookEventType] | None | Unset = UNSET
    filter_paths: list[ResourceField] | None | Unset = UNSET
    secret: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = str(self.id)

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        url = self.url

        event_types: list[str] | None | Unset
        if isinstance(self.event_types, Unset):
            event_types = UNSET
        elif isinstance(self.event_types, list):
            event_types = []
            for event_types_type_0_item_data in self.event_types:
                event_types_type_0_item = event_types_type_0_item_data.value
                event_types.append(event_types_type_0_item)

        else:
            event_types = self.event_types

        filter_paths: list[str] | None | Unset
        if isinstance(self.filter_paths, Unset):
            filter_paths = UNSET
        elif isinstance(self.filter_paths, list):
            filter_paths = []
            for filter_paths_type_0_item_data in self.filter_paths:
                filter_paths_type_0_item = filter_paths_type_0_item_data.value
                filter_paths.append(filter_paths_type_0_item)

        else:
            filter_paths = self.filter_paths

        secret: None | str | Unset
        if isinstance(self.secret, Unset):
            secret = UNSET
        else:
            secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "status": status,
                "updatedAt": updated_at,
                "url": url,
            }
        )
        if event_types is not UNSET:
            field_dict["eventTypes"] = event_types
        if filter_paths is not UNSET:
            field_dict["filterPaths"] = filter_paths
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        id = UUID(d.pop("id"))

        status = ApiWebhookStatus(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        url = d.pop("url")

        def _parse_event_types(data: object) -> list[WebhookEventType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_types_type_0 = []
                _event_types_type_0 = data
                for event_types_type_0_item_data in _event_types_type_0:
                    event_types_type_0_item = WebhookEventType(event_types_type_0_item_data)

                    event_types_type_0.append(event_types_type_0_item)

                return event_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[WebhookEventType] | None | Unset, data)

        event_types = _parse_event_types(d.pop("eventTypes", UNSET))

        def _parse_filter_paths(data: object) -> list[ResourceField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_paths_type_0 = []
                _filter_paths_type_0 = data
                for filter_paths_type_0_item_data in _filter_paths_type_0:
                    filter_paths_type_0_item = ResourceField(filter_paths_type_0_item_data)

                    filter_paths_type_0.append(filter_paths_type_0_item)

                return filter_paths_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ResourceField] | None | Unset, data)

        filter_paths = _parse_filter_paths(d.pop("filterPaths", UNSET))

        def _parse_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret = _parse_secret(d.pop("secret", UNSET))

        api_webhook_response = cls(
            created_at=created_at,
            id=id,
            status=status,
            updated_at=updated_at,
            url=url,
            event_types=event_types,
            filter_paths=filter_paths,
            secret=secret,
        )

        api_webhook_response.additional_properties = d
        return api_webhook_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
