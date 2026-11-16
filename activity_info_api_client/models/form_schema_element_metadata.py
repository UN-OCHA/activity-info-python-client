from enum import Enum


class FormSchemaElementMetadata(str, Enum):
    ADDED_BY = "ADDED_BY"
    LAST_EDITED_BY = "LAST_EDITED_BY"

    def __str__(self) -> str:
        return str(self.value)
