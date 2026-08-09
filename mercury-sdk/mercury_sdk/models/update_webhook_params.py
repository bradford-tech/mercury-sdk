from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_field import ResourceField
from ..models.webhook_event_type import WebhookEventType
from ..models.webhook_update_status import WebhookUpdateStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWebhookParams")


@_attrs_define
class UpdateWebhookParams:
    """Request body for updating an existing webhook endpoint.
    All fields are optional - only provided fields will be updated.

       Attributes:
           event_types (list[WebhookEventType] | None | Unset):  Event types to subscribe to. Send null to subscribe to all
               event types. Send an array to subscribe to specific types. Omit to leave unchanged.
           filter_paths (list[ResourceField] | None | Unset):  Resource field paths to filter events by. When specified,
               webhook events will only be sent when one of these fields changes. Send null for no filtering. Send an array to
               filter by specific fields. Omit to leave unchanged.
           status (None | Unset | WebhookUpdateStatus):  Webhook status. Only 'active' and 'paused' values are allowed.
               Omit to leave unchanged.
           url (None | str | Unset):  The URL to which webhook events will be delivered. Omit to leave unchanged.
    """

    event_types: list[WebhookEventType] | None | Unset = UNSET
    filter_paths: list[ResourceField] | None | Unset = UNSET
    status: None | Unset | WebhookUpdateStatus = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, WebhookUpdateStatus):
            status = self.status.value
        else:
            status = self.status

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_types is not UNSET:
            field_dict["eventTypes"] = event_types
        if filter_paths is not UNSET:
            field_dict["filterPaths"] = filter_paths
        if status is not UNSET:
            field_dict["status"] = status
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_status(data: object) -> None | Unset | WebhookUpdateStatus:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = WebhookUpdateStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WebhookUpdateStatus, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        update_webhook_params = cls(
            event_types=event_types,
            filter_paths=filter_paths,
            status=status,
            url=url,
        )

        update_webhook_params.additional_properties = d
        return update_webhook_params

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
