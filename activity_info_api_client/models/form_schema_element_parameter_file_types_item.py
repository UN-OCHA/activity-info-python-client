from enum import Enum


class FormSchemaElementParameterFileTypesItem(str, Enum):
    AUDIO = "AUDIO"
    IMAGE = "IMAGE"
    OFFICE_DOCUMENT = "OFFICE_DOCUMENT"
    PDF = "PDF"
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
