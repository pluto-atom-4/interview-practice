import pytest

from ood.design_patterns.observer import (EmailSubscriber, NewsPublisher,
                                          SMSSubscriber)


def test_observer_notification():
    publisher = NewsPublisher()
    email = EmailSubscriber()
    sms = SMSSubscriber()

    publisher.attach(email)
    publisher.attach(sms)

    publisher.notify("Breaking News!")

    assert email.inbox == ["Email received: Breaking News!"]
    assert sms.messages == ["SMS received: Breaking News!"]


def test_observer_detach():
    publisher = NewsPublisher()
    email = EmailSubscriber()
    sms = SMSSubscriber()

    publisher.attach(email)
    publisher.attach(sms)
    publisher.detach(sms)

    publisher.notify("Market Update")

    assert email.inbox == ["Email received: Market Update"]
    assert sms.messages == []  # SMS was detached
