from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_record_fields import FormRecordFields


T = TypeVar("T", bound="FormRecord")


@_attrs_define
class FormRecord:
    """
    Attributes:
        form_id (str):
        record_id (str):
        last_edit_time (float):
        fields (FormRecordFields):
        parent_record_id (str | Unset):
    """

    form_id: str
    record_id: str
    last_edit_time: float
    fields: FormRecordFields
    parent_record_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        form_id = self.form_id

        record_id = self.record_id

        last_edit_time = self.last_edit_time

        fields = self.fields.to_dict()

        parent_record_id = self.parent_record_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formId": form_id,
                "recordId": record_id,
                "lastEditTime": last_edit_time,
                "fields": fields,
            }
        )
        if parent_record_id is not UNSET:
            field_dict["parentRecordId"] = parent_record_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_record_fields import FormRecordFields

        d = dict(src_dict)
        form_id = d.pop("formId")

        record_id = d.pop("recordId")

        last_edit_time = d.pop("lastEditTime")

        fields = FormRecordFields.from_dict(d.pop("fields"))

        parent_record_id = d.pop("parentRecordId", UNSET)

        form_record = cls(
            form_id=form_id,
            record_id=record_id,
            last_edit_time=last_edit_time,
            fields=fields,
            parent_record_id=parent_record_id,
        )

        form_record.additional_properties = d
        return form_record

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
