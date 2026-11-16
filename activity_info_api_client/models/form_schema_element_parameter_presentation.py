from enum import Enum


class FormSchemaElementParameterPresentation(str, Enum):
    AUTOMATIC = "automatic"
    DROPDOWN = "dropdown"
    RADIO_BUTTON = "radio_button"

    def __str__(self) -> str:
        return str(self.value)
