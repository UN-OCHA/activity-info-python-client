from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_permissions import FormPermissions
    from ..models.form_schema import FormSchema


T = TypeVar("T", bound="Form")


@_attrs_define
class Form:
    """
    Attributes:
        id (str): The id of the form
        permissions (FormPermissions):
        schema (FormSchema | Unset):
        schema_version (int | Unset): Server-assigned schema version, omitted when the form is deleted or inaccessible.
        visible (bool | Unset): True if the form is visible to the authenticated user
        deleted (bool | Unset): True if the form has been deleted
        suspended (bool | Unset): True if the form belongs to a suspended database.
    """

    id: str
    permissions: FormPermissions
    schema: FormSchema | Unset = UNSET
    schema_version: int | Unset = UNSET
    visible: bool | Unset = UNSET
    deleted: bool | Unset = UNSET
    suspended: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        permissions = self.permissions.to_dict()

        schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        schema_version = self.schema_version

        visible = self.visible

        deleted = self.deleted

        suspended = self.suspended

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "permissions": permissions,
            }
        )
        if schema is not UNSET:
            field_dict["schema"] = schema
        if schema_version is not UNSET:
            field_dict["schemaVersion"] = schema_version
        if visible is not UNSET:
            field_dict["visible"] = visible
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if suspended is not UNSET:
            field_dict["suspended"] = suspended

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_permissions import FormPermissions
        from ..models.form_schema import FormSchema

        d = dict(src_dict)
        id = d.pop("id")

        permissions = FormPermissions.from_dict(d.pop("permissions"))

        _schema = d.pop("schema", UNSET)
        schema: FormSchema | Unset
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = FormSchema.from_dict(_schema)

        schema_version = d.pop("schemaVersion", UNSET)

        visible = d.pop("visible", UNSET)

        deleted = d.pop("deleted", UNSET)

        suspended = d.pop("suspended", UNSET)

        form = cls(
            id=id,
            permissions=permissions,
            schema=schema,
            schema_version=schema_version,
            visible=visible,
            deleted=deleted,
            suspended=suspended,
        )

        form.additional_properties = d
        return form

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
