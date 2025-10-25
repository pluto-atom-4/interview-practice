"""
Observer Design Pattern
----------------------------------------------
- Intent: Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified.
- Use Case: UI event listeners, pub-sub systems, logging, data binding.
"""

# NOTE:
# ABC stands for Abstract Base Class, provided by Python's `abc` module.
# It allows us to define interfaces with abstract methods that must be implemented by subclasses.
# By inheriting from ABC and using the @abstractmethod decorator, we enforce a contract:
# any subclass must implement the required methods, or it cannot be instantiated.
# This is useful for defining consistent behavior across multiple implementations — like Observer or Strategy patterns.

from abc import ABC, abstractmethod
from typing import List


# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass


# Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        pass


# Concrete Subject
class NewsPublisher(Subject):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)


# Concrete Observers
class EmailSubscriber(Observer):
    def __init__(self):
        self.inbox: List[str] = []

    def update(self, message: str) -> None:
        self.inbox.append(f"Email received: {message}")


class SMSSubscriber(Observer):
    def __init__(self):
        self.messages: List[str] = []

    def update(self, message: str) -> None:
        self.messages.append(f"SMS received: {message}")
