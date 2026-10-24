
from .payment_factory import PaymentFactory
from .adyen_authorizer import AdyenAuthorizer
from .adyen_refund_processor import AdyenRefundProcessor
from .adyen_webhook_verifier import AdyenWebhookVerifier


class AdyenFactory(PaymentFactory):
    def create_authorizer(self) -> AdyenAuthorizer:
        return AdyenAuthorizer()

    def create_refund_processor(self) -> AdyenRefundProcessor:
        return AdyenRefundProcessor()

    def create_webhook_verifier(self) -> AdyenWebhookVerifier:
        return AdyenWebhookVerifier()
