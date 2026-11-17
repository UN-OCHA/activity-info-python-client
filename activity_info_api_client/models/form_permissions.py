from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_lock import DatabaseLock
    from ..models.field_condition import FieldCondition


T = TypeVar("T", bound="FormPermissions")


@_attrs_define
class FormPermissions:
    """
    Attributes:
        view (bool):
        create_record (bool):
        edit_record (bool):
        delete_record (bool):
        view_filter (None | str | Unset):
        create_filter (None | str | Unset):
        edit_filter (None | str | Unset):
        delete_filter (None | str | Unset):
        bulk_delete (bool | Unset):
        export_records (bool | Unset):
        resolve_duplicates (bool | Unset):
        update_schema (bool | Unset):
        collection_links (bool | Unset):
        public_form (bool | Unset):
        api (bool | Unset):
        security_categories (list[str] | Unset):
        locks (list[DatabaseLock] | Unset):
        field_level_conditions (list[FieldCondition] | Unset):
        manage_import_configurations (bool | Unset):
    """

    view: bool
    create_record: bool
    edit_record: bool
    delete_record: bool
    view_filter: None | str | Unset = UNSET
    create_filter: None | str | Unset = UNSET
    edit_filter: None | str | Unset = UNSET
    delete_filter: None | str | Unset = UNSET
    bulk_delete: bool | Unset = UNSET
    export_records: bool | Unset = UNSET
    resolve_duplicates: bool | Unset = UNSET
    update_schema: bool | Unset = UNSET
    collection_links: bool | Unset = UNSET
    public_form: bool | Unset = UNSET
    api: bool | Unset = UNSET
    security_categories: list[str] | Unset = UNSET
    locks: list[DatabaseLock] | Unset = UNSET
    field_level_conditions: list[FieldCondition] | Unset = UNSET
    manage_import_configurations: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        view = self.view

        create_record = self.create_record

        edit_record = self.edit_record

        delete_record = self.delete_record

        view_filter: None | str | Unset
        if isinstance(self.view_filter, Unset):
            view_filter = UNSET
        else:
            view_filter = self.view_filter

        create_filter: None | str | Unset
        if isinstance(self.create_filter, Unset):
            create_filter = UNSET
        else:
            create_filter = self.create_filter

        edit_filter: None | str | Unset
        if isinstance(self.edit_filter, Unset):
            edit_filter = UNSET
        else:
            edit_filter = self.edit_filter

        delete_filter: None | str | Unset
        if isinstance(self.delete_filter, Unset):
            delete_filter = UNSET
        else:
            delete_filter = self.delete_filter

        bulk_delete = self.bulk_delete

        export_records = self.export_records

        resolve_duplicates = self.resolve_duplicates

        update_schema = self.update_schema

        collection_links = self.collection_links

        public_form = self.public_form

        api = self.api

        security_categories: list[str] | Unset = UNSET
        if not isinstance(self.security_categories, Unset):
            security_categories = self.security_categories

        locks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.locks, Unset):
            locks = []
            for locks_item_data in self.locks:
                locks_item = locks_item_data.to_dict()
                locks.append(locks_item)

        field_level_conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.field_level_conditions, Unset):
            field_level_conditions = []
            for field_level_conditions_item_data in self.field_level_conditions:
                field_level_conditions_item = field_level_conditions_item_data.to_dict()
                field_level_conditions.append(field_level_conditions_item)

        manage_import_configurations = self.manage_import_configurations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "view": view,
                "createRecord": create_record,
                "editRecord": edit_record,
                "deleteRecord": delete_record,
            }
        )
        if view_filter is not UNSET:
            field_dict["viewFilter"] = view_filter
        if create_filter is not UNSET:
            field_dict["createFilter"] = create_filter
        if edit_filter is not UNSET:
            field_dict["editFilter"] = edit_filter
        if delete_filter is not UNSET:
            field_dict["deleteFilter"] = delete_filter
        if bulk_delete is not UNSET:
            field_dict["bulkDelete"] = bulk_delete
        if export_records is not UNSET:
            field_dict["exportRecords"] = export_records
        if resolve_duplicates is not UNSET:
            field_dict["resolveDuplicates"] = resolve_duplicates
        if update_schema is not UNSET:
            field_dict["updateSchema"] = update_schema
        if collection_links is not UNSET:
            field_dict["collectionLinks"] = collection_links
        if public_form is not UNSET:
            field_dict["publicForm"] = public_form
        if api is not UNSET:
            field_dict["api"] = api
        if security_categories is not UNSET:
            field_dict["securityCategories"] = security_categories
        if locks is not UNSET:
            field_dict["locks"] = locks
        if field_level_conditions is not UNSET:
            field_dict["fieldLevelConditions"] = field_level_conditions
        if manage_import_configurations is not UNSET:
            field_dict["manageImportConfigurations"] = manage_import_configurations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_lock import DatabaseLock
        from ..models.field_condition import FieldCondition

        d = dict(src_dict)
        view = d.pop("view")

        create_record = d.pop("createRecord")

        edit_record = d.pop("editRecord")

        delete_record = d.pop("deleteRecord")

        def _parse_view_filter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        view_filter = _parse_view_filter(d.pop("viewFilter", UNSET))

        def _parse_create_filter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        create_filter = _parse_create_filter(d.pop("createFilter", UNSET))

        def _parse_edit_filter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edit_filter = _parse_edit_filter(d.pop("editFilter", UNSET))

        def _parse_delete_filter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delete_filter = _parse_delete_filter(d.pop("deleteFilter", UNSET))

        bulk_delete = d.pop("bulkDelete", UNSET)

        export_records = d.pop("exportRecords", UNSET)

        resolve_duplicates = d.pop("resolveDuplicates", UNSET)

        update_schema = d.pop("updateSchema", UNSET)

        collection_links = d.pop("collectionLinks", UNSET)

        public_form = d.pop("publicForm", UNSET)

        api = d.pop("api", UNSET)

        security_categories = cast(list[str], d.pop("securityCategories", UNSET))

        _locks = d.pop("locks", UNSET)
        locks: list[DatabaseLock] | Unset = UNSET
        if _locks is not UNSET:
            locks = []
            for locks_item_data in _locks:
                locks_item = DatabaseLock.from_dict(locks_item_data)

                locks.append(locks_item)

        _field_level_conditions = d.pop("fieldLevelConditions", UNSET)
        field_level_conditions: list[FieldCondition] | Unset = UNSET
        if _field_level_conditions is not UNSET:
            field_level_conditions = []
            for field_level_conditions_item_data in _field_level_conditions:
                field_level_conditions_item = FieldCondition.from_dict(field_level_conditions_item_data)

                field_level_conditions.append(field_level_conditions_item)

        manage_import_configurations = d.pop("manageImportConfigurations", UNSET)

        form_permissions = cls(
            view=view,
            create_record=create_record,
            edit_record=edit_record,
            delete_record=delete_record,
            view_filter=view_filter,
            create_filter=create_filter,
            edit_filter=edit_filter,
            delete_filter=delete_filter,
            bulk_delete=bulk_delete,
            export_records=export_records,
            resolve_duplicates=resolve_duplicates,
            update_schema=update_schema,
            collection_links=collection_links,
            public_form=public_form,
            api=api,
            security_categories=security_categories,
            locks=locks,
            field_level_conditions=field_level_conditions,
            manage_import_configurations=manage_import_configurations,
        )

        form_permissions.additional_properties = d
        return form_permissions

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
