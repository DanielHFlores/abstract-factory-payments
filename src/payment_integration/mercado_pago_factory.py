
from .payment_factory import PaymentFactory
from .mercado_pago_authorizer import MercadoPagoAuthorizer
from .mercado_pago_refund_processor import MercadoPagoRefundProcessor
from .mercado_pago_webhook_verifier import MercadoPagoWebhookVerifier


class MercadoPagoFactory(PaymentFactory):
    def create_authorizer(self) -> MercadoPagoAuthorizer:
        return MercadoPagoAuthorizer()

    def create_refund_processor(self) -> MercadoPagoRefundProcessor:
        return MercadoPagoRefundProcessor()

    def create_webhook_verifier(self) -> MercadoPagoWebhookVerifier:
        return MercadoPagoWebhookVerifier()
