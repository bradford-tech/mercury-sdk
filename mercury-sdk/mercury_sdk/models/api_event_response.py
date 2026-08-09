from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_event_operation_type import ApiEventOperationType
from ..models.api_event_resource_type import ApiEventResourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_event_response_merge_patch import ApiEventResponseMergePatch
    from ..models.api_event_response_previous_values_type_0 import ApiEventResponsePreviousValuesType0


T = TypeVar("T", bound="ApiEventResponse")


@_attrs_define
class ApiEventResponse:
    """Represents a single event in the Mercury API event stream.
    Events track changes to resources over time, providing an audit trail
    of all modifications with before/after values and metadata about what changed.

       Attributes:
           changed_paths (list[str]):  List of JSON paths that were modified in this event
           id (UUID):  Unique identifier for this event
           merge_patch (ApiEventResponseMergePatch):  JSON object containing the fields that were changed and their new
               values
           occurred_at (datetime.datetime):  Timestamp when the event occurred Example: 2016-07-22T00:00:00Z.
           operation_type (ApiEventOperationType):
           resource_id (UUID):  The ID of the resource that was affected Example: 00000000-0000-0000-0000-000000000000.
           resource_type (ApiEventResourceType):
           resource_version (int):  Version number of the resource after this change
           previous_values (ApiEventResponsePreviousValuesType0 | None | Unset):  JSON object containing the fields that
               were changed and their previous values before the update
    """

    changed_paths: list[str]
    id: UUID
    merge_patch: ApiEventResponseMergePatch
    occurred_at: datetime.datetime
    operation_type: ApiEventOperationType
    resource_id: UUID
    resource_type: ApiEventResourceType
    resource_version: int
    previous_values: ApiEventResponsePreviousValuesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_event_response_previous_values_type_0 import ApiEventResponsePreviousValuesType0

        changed_paths = self.changed_paths

        id = str(self.id)

        merge_patch = self.merge_patch.to_dict()

        occurred_at = self.occurred_at.isoformat()

        operation_type = self.operation_type.value

        resource_id = str(self.resource_id)

        resource_type = self.resource_type.value

        resource_version = self.resource_version

        previous_values: dict[str, Any] | None | Unset
        if isinstance(self.previous_values, Unset):
            previous_values = UNSET
        elif isinstance(self.previous_values, ApiEventResponsePreviousValuesType0):
            previous_values = self.previous_values.to_dict()
        else:
            previous_values = self.previous_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changedPaths": changed_paths,
                "id": id,
                "mergePatch": merge_patch,
                "occurredAt": occurred_at,
                "operationType": operation_type,
                "resourceId": resource_id,
                "resourceType": resource_type,
                "resourceVersion": resource_version,
            }
        )
        if previous_values is not UNSET:
            field_dict["previousValues"] = previous_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_event_response_merge_patch import ApiEventResponseMergePatch
        from ..models.api_event_response_previous_values_type_0 import ApiEventResponsePreviousValuesType0

        d = dict(src_dict)
        changed_paths = cast(list[str], d.pop("changedPaths"))

        id = UUID(d.pop("id"))

        merge_patch = ApiEventResponseMergePatch.from_dict(d.pop("mergePatch"))

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurredAt"))

        operation_type = ApiEventOperationType(d.pop("operationType"))

        resource_id = UUID(d.pop("resourceId"))

        resource_type = ApiEventResourceType(d.pop("resourceType"))

        resource_version = d.pop("resourceVersion")

        def _parse_previous_values(data: object) -> ApiEventResponsePreviousValuesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                previous_values_type_0 = ApiEventResponsePreviousValuesType0.from_dict(data)

                return previous_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiEventResponsePreviousValuesType0 | None | Unset, data)

        previous_values = _parse_previous_values(d.pop("previousValues", UNSET))

        api_event_response = cls(
            changed_paths=changed_paths,
            id=id,
            merge_patch=merge_patch,
            occurred_at=occurred_at,
            operation_type=operation_type,
            resource_id=resource_id,
            resource_type=resource_type,
            resource_version=resource_version,
            previous_values=previous_values,
        )

        api_event_response.additional_properties = d
        return api_event_response

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
