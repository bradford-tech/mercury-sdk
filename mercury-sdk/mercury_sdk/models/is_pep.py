from enum import Enum


class IsPep(str, Enum):
    ISNOTPEP = "IsNotPep"
    ISPEP = "IsPep"

    def __str__(self) -> str:
        return str(self.value)
