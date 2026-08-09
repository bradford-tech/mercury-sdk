from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_field import ResourceField
from ..models.webhook_event_type import WebhookEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebhookParams")


@_attrs_define
class CreateWebhookParams:
    """Request body for creating a new webhook endpoint

    Attributes:
        url (str):  The URL to which webhook events will be delivered
        event_types (list[WebhookEventType] | None | Unset):  Optional array of event types to subscribe to. Nothing
            means subscribe to all event types.
        filter_paths (list[ResourceField] | None | Unset):  Optional array of resource field paths to filter events by.
            When specified, webhook events will only be sent when one of these fields changes. Nothing means no filtering
            (all events are sent).
    """

    url: str
    event_types: list[WebhookEventType] | None | Unset = UNSET
    filter_paths: list[ResourceField] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if event_types is not UNSET:
            field_dict["eventTypes"] = event_types
        if filter_paths is not UNSET:
            field_dict["filterPaths"] = filter_paths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        create_webhook_params = cls(
            url=url,
            event_types=event_types,
            filter_paths=filter_paths,
        )

        create_webhook_params.additional_properties = d
        return create_webhook_params

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
