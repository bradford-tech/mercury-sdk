from enum import Enum


class ValuationType(str, Enum):
    NOVALUATION = "NoValuation"
    POSTMONEY = "PostMoney"
    PREMONEY = "PreMoney"

    def __str__(self) -> str:
        return str(self.value)
