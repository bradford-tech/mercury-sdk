from enum import Enum


class AccountType(str, Enum):
    EXTERNAL = "external"
    MERCURY = "mercury"
    RECIPIENT = "recipient"

    def __str__(self) -> str:
        return str(self.value)
