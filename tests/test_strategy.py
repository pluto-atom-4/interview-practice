import pytest

from ood.design_patterns.strategy import (BitcoinPayment, CreditCardPayment,
                                          PaymentProcessor, PayPalPayment)


def test_credit_card_payment():
    processor = PaymentProcessor(CreditCardPayment())
    result = processor.process_payment(100.0)
    assert result == "Paid $100.00 using Credit Card."


def test_paypal_payment():
    processor = PaymentProcessor(PayPalPayment())
    result = processor.process_payment(50.5)
    assert result == "Paid $50.50 using PayPal."


def test_bitcoin_payment():
    processor = PaymentProcessor(BitcoinPayment())
    result = processor.process_payment(0.01)
    assert result == "Paid $0.01 using Bitcoin."


def test_strategy_switching():
    processor = PaymentProcessor(CreditCardPayment())
    assert processor.process_payment(20) == "Paid $20.00 using Credit Card."
    processor.set_strategy(BitcoinPayment())
    assert processor.process_payment(20) == "Paid $20.00 using Bitcoin."
