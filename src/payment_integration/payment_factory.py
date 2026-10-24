
from abc import ABC, abstractmethod

from .payment_authorizer import PaymentAuthorizer
from .refund_processor import RefundProcessor
from .webhook_verifier import WebhookVerifier


class PaymentFactory(ABC):
    @abstractmethod
    def create_authorizer(self) -> PaymentAuthorizer:
        pass

    @abstractmethod
    def create_refund_processor(self) -> RefundProcessor:
        pass

    @abstractmethod
    def create_webhook_verifier(self) -> WebhookVerifier:
        pass
