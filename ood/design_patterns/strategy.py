"""
Strategy Design Pattern Example: Payment Processing
This example demonstrates the Strategy Design Pattern by implementing different payment methods.
The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
It allows the algorithm to vary independently of clients that use it.
"""

from abc import ABC, abstractmethod


# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using Credit Card."


class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using PayPal."


class BitcoinPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using Bitcoin."


# Context
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount: float) -> str:
        return self.strategy.pay(amount)
