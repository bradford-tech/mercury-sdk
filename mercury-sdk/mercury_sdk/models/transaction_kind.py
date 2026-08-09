from enum import Enum


class TransactionKind(str, Enum):
    BILLINGENGINESUBSCRIPTIONFEE = "billingEngineSubscriptionFee"
    CARDINTERNATIONALTRANSACTIONFEE = "cardInternationalTransactionFee"
    CARDINTERNATIONALTRANSACTIONFEEREBATE = "cardInternationalTransactionFeeRebate"
    CARDINTERNATIONALTRANSACTIONFEEREBATEREVERSAL = "cardInternationalTransactionFeeRebateReversal"
    CARDINTERNATIONALTRANSACTIONFEEREVERSAL = "cardInternationalTransactionFeeReversal"
    CHECKDEPOSIT = "checkDeposit"
    CREDITCARDCREDIT = "creditCardCredit"
    CREDITCARDTRANSACTION = "creditCardTransaction"
    CURRENCYCLOUDRETURN = "currencyCloudReturn"
    DEBITCARDCREDIT = "debitCardCredit"
    DEBITCARDTRANSACTION = "debitCardTransaction"
    EXOGENOUSWIREDRAWDOWN = "exogenousWireDrawdown"
    EXPENSEREIMBURSEMENT = "expenseReimbursement"
    EXTERNALTRANSFER = "externalTransfer"
    INCOMINGDOMESTICWIRE = "incomingDomesticWire"
    INCOMINGINTERNATIONALWIRE = "incomingInternationalWire"
    INTERESTPAYMENT = "interestPayment"
    INTERNALTRANSFER = "internalTransfer"
    OTHER = "other"
    OUTGOINGPAYMENT = "outgoingPayment"
    PERSONALBANKINGSUBSCRIPTIONFEE = "personalBankingSubscriptionFee"
    TREASURYTRANSFER = "treasuryTransfer"
    WIREFEE = "wireFee"

    def __str__(self) -> str:
        return str(self.value)
