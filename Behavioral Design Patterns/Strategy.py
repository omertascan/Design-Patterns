from abc import ABC, abstractmethod

# Strategy 
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# ConcreteStrategy 
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Kredi Kartı ile ${amount} ödeme yapılıyor.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"PayPal ile ${amount} ödeme yapılıyor.")

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Banka Havalesi ile ${amount} ödeme yapılıyor.")

# Context 
class PaymentContext:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def perform_payment(self, amount):
        self.payment_strategy.pay(amount)

if __name__ == "__main__":
    # Farklı ödeme stratejileri ile ödeme işlemleri gerçekleştirme
    credit_card = CreditCardPayment()
    paypal = PayPalPayment()
    bank_transfer = BankTransferPayment()

    payment_context = PaymentContext(credit_card)
    payment_context.perform_payment(100)

    payment_context = PaymentContext(paypal)
    payment_context.perform_payment(50)

    payment_context = PaymentContext(bank_transfer)
    payment_context.perform_payment(200)


