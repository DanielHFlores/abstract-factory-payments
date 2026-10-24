
from .payment_factory import PaymentFactory
from .stripe_authorizer import StripeAuthorizer
from .stripe_refund_processor import StripeRefundProcessor
from .stripe_webhook_verifier import StripeWebhookVerifier


class StripeFactory(PaymentFactory):
    def create_authorizer(self) -> StripeAuthorizer:
        return StripeAuthorizer()

    def create_refund_processor(self) -> StripeRefundProcessor:
        return StripeRefundProcessor()

    def create_webhook_verifier(self) -> StripeWebhookVerifier:
        return StripeWebhookVerifier()
