import pytest

from ood.design_patterns.decorator import (BasicNotifier, EmailDecorator,
                                           SlackDecorator, SMSDecorator)


def test_basic_notifier():
    notifier = BasicNotifier()
    result = notifier.send("Hello")
    assert result == "Basic Notification: Hello"

def test_sms_decorator():
    notifier = SMSDecorator(BasicNotifier())
    result = notifier.send("Hello")
    assert "SMS sent: Hello" in result

def test_email_decorator():
    notifier = EmailDecorator(BasicNotifier())
    result = notifier.send("Hello")
    assert "Email sent: Hello" in result

def test_combined_decorators():
    notifier = SlackDecorator(EmailDecorator(SMSDecorator(BasicNotifier())))
    result = notifier.send("Hello")
    assert "Basic Notification: Hello" in result
    assert "SMS sent: Hello" in result
    assert "Email sent: Hello" in result
    assert "Slack message sent: Hello" in result

def test_decorator_chain_structure():
    notifier = SlackDecorator(EmailDecorator(SMSDecorator(BasicNotifier())))
    chain = []
    current = notifier
    while hasattr(current, "_notifier"):
        chain.append(type(current).__name__)
        current = current._notifier
    chain.append(type(current).__name__)
    assert chain == ["SlackDecorator", "EmailDecorator", "SMSDecorator", "BasicNotifier"]