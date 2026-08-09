from enum import Enum


class ApiSendEmailOption(str, Enum):
    DONTSEND = "DontSend"
    SENDNOW = "SendNow"

    def __str__(self) -> str:
        return str(self.value)
