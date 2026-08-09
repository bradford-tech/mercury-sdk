from enum import Enum


class TreasuryTransactionType(str, Enum):
    DEPOSITCANCELED = "depositCanceled"
    DEPOSITCOMPLETE = "depositComplete"
    DEPOSITFAILED = "depositFailed"
    DEPOSITRETURNED = "depositReturned"
    DIVIDENDCANCELED = "dividendCanceled"
    DIVIDENDPOSTED = "dividendPosted"
    DIVIDENDREINVESTMENTPOSTED = "dividendReinvestmentPosted"
    INTERESTCANCELED = "interestCanceled"
    INTERESTPOSTED = "interestPosted"
    MANUALAMENDMENTPOSTED = "manualAmendmentPosted"
    MERCURYCREDITFAILED = "mercuryCreditFailed"
    MERCURYCREDITPOSTED = "mercuryCreditPosted"
    MERCURYFEECANCELED = "mercuryFeeCanceled"
    MERCURYFEEFAILED = "mercuryFeeFailed"
    MERCURYFEEPOSTED = "mercuryFeePosted"
    MERCURYFEEREFUNDED = "mercuryFeeRefunded"
    MUTUALFUNDTRADEFAILED = "mutualFundTradeFailed"
    MUTUALFUNDTRADEPOSTED = "mutualFundTradePosted"
    OEMSMUTUALFUNDORDERCANCELED = "oemsMutualFundOrderCanceled"
    OEMSMUTUALFUNDORDERREJECTED = "oemsMutualFundOrderRejected"
    OEMSMUTUALFUNDORDERSETTLED = "oemsMutualFundOrderSettled"
    REVERTTXN = "revertTxn"
    SWEEPINPOSTED = "sweepInPosted"
    SWEEPOUTPOSTED = "sweepOutPosted"
    SWEEPRECONCILEPOSTED = "sweepReconcilePosted"
    VALUATIONCHANGEPOSTED = "valuationChangePosted"
    WITHDRAWALCANCELED = "withdrawalCanceled"
    WITHDRAWALFAILED = "withdrawalFailed"
    WITHDRAWALPOSTED = "withdrawalPosted"
    WITHDRAWALRETURNED = "withdrawalReturned"

    def __str__(self) -> str:
        return str(self.value)
