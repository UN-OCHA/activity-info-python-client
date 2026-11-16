from enum import Enum


class FormSchemaElementParameterCaptureMethodsItem(str, Enum):
    AUDIO = "AUDIO"
    CAMERA = "CAMERA"
    FILE = "FILE"
    SIGNATURE = "SIGNATURE"

    def __str__(self) -> str:
        return str(self.value)
