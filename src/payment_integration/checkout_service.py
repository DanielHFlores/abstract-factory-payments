
from .payment_factory import PaymentFactory


class CheckoutService:
    def __init__(self, factory: PaymentFactory):
        self.authorizer = factory.create_authorizer()
        self.refunds = factory.create_refund_processor()
        self.webhooks = factory.create_webhook_verifier()

    def authorize_payment(self, amount: float) -> str:
        return self.authorizer.authorize(amount)

    def refund_payment(self, amount: float) -> str:
        return self.refunds.refund(amount)

    def verify_webhook(self, signature: str) -> bool:
        return self.webhooks.verify(signature)
