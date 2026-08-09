from enum import Enum


class TreasuryStatementDocumentType(str, Enum):
    FMV = "FMV"
    MONTHLYSTATEMENT = "MonthlyStatement"
    SDIRA = "SDIRA"
    TRADECONFIRMATION = "TradeConfirmation"
    VALUE_2 = "1099"
    VALUE_3 = "1099R"
    VALUE_4 = "1042S"
    VALUE_5 = "5498"
    VALUE_6 = "5498ESA"
    VALUE_7 = "1099Q"

    def __str__(self) -> str:
        return str(self.value)
