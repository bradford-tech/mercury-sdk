from enum import Enum


class TransactionRelationKind(str, Enum):
    ATMREIMBURSEMENTREVERSALTOATMTRANSACTION = "AtmReimbursementReversalToAtmTransaction"
    ATMTRANSACTIONTOATMREIMBURSEMENTREVERSAL = "AtmTransactionToAtmReimbursementReversal"
    ATMTRANSACTIONTOFEEATMREIMBURSEMENT = "AtmTransactionToFeeAtmReimbursement"
    FAILEDPAYMENTTOPAYMENTREFUND = "FailedPaymentToPaymentRefund"
    FEEATMREIMBURSEMENTTOATMTRANSACTION = "FeeAtmReimbursementToAtmTransaction"
    FEEPAYMENTTOFEEREBATE = "FeePaymentToFeeRebate"
    FEEPAYMENTTOFEEREVERSAL = "FeePaymentToFeeReversal"
    FEEPAYMENTTOORIGINALTRANSACTION = "FeePaymentToOriginalTransaction"
    FEEREBATEREVERSALTOFEEREBATE = "FeeRebateReversalToFeeRebate"
    FEEREBATETOFEEPAYMENT = "FeeRebateToFeePayment"
    FEEREBATETOFEEREBATEREVERSAL = "FeeRebateToFeeRebateReversal"
    FEEREVERSALTOFEEPAYMENT = "FeeReversalToFeePayment"
    FRAUDULENTCHARGETOMERCHANTREFUND = "FraudulentChargeToMerchantRefund"
    GIFTCOMPENSATIONTOORIGINALTRANSACTION = "GiftCompensationToOriginalTransaction"
    MERCHANTREFUNDTOFRAUDULENTCHARGE = "MerchantRefundToFraudulentCharge"
    MERCHANTREFUNDTOORIGINALCHARGE = "MerchantRefundToOriginalCharge"
    MERCHANTREFUNDTOPROVISIONALCREDITREVERSAL = "MerchantRefundToProvisionalCreditReversal"
    ORIGINALCHARGETOMERCHANTREFUND = "OriginalChargeToMerchantRefund"
    ORIGINALCHARGETOPROVISIONALCREDIT = "OriginalChargeToProvisionalCredit"
    ORIGINALTRANSACTIONTOFEEPAYMENT = "OriginalTransactionToFeePayment"
    ORIGINALTRANSACTIONTORETURN = "OriginalTransactionToReturn"
    PAYMENTREFUNDTOFAILEDPAYMENT = "PaymentRefundToFailedPayment"
    PROVISIONALCREDITREVERSALTOMERCHANTREFUND = "ProvisionalCreditReversalToMerchantRefund"
    PROVISIONALCREDITTOORIGINALCHARGE = "ProvisionalCreditToOriginalCharge"
    PROVISIONALCREDITTOREVERSAL = "ProvisionalCreditToReversal"
    RETURNTOORIGINALTRANSACTION = "ReturnToOriginalTransaction"
    REVERSALTOPROVISIONALCREDIT = "ReversalToProvisionalCredit"
    TREASURYSPLITLIQUIDATION = "TreasurySplitLiquidation"

    def __str__(self) -> str:
        return str(self.value)
