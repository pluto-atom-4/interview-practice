"""
Observer Design Pattern Explained Step-by-Step
----------------------------------------------
The Observer Design Pattern is a behavioral design pattern that defines a one-to-many dependency
between objects so that when one object changes state, all its dependents are notified and updated
automatically. This pattern is essential for implementing distributed event handling systems and
maintaining loose coupling between components. It's commonly used in Model-View architectures,
event-driven systems, and any scenario where multiple objects need to react to state changes
in another object without creating tight dependencies.

Here is how the process works:

1. **Subject Interface**: Define the interface for objects that can be observed.
   - Abstract base class that manages observer relationships
   - Provides methods to attach, detach, and notify observers
   - Maintains a list of dependent observer objects
   - Ensures consistent observer management across all concrete subjects

2. **Observer Interface**: Define the interface for objects that should be notified of changes.
   - Abstract base class with update method that observers must implement
   - Declares the notification interface that all observers will follow
   - Ensures all observers can receive and process notifications consistently
   - Provides the contract that subject class depends on for notifications

3. **Concrete Subject**: Implement the subject interface and manage observer state.
   - Maintains the list of registered observers
   - Implements attach/detach methods to manage observer registration
   - Stores the state that observers are interested in monitoring
   - Triggers notifications when state changes occur

4. **Observer Registration**: Observers register themselves with the subject.
   - Observers call attach() method to subscribe to notifications
   - Subject adds observer to its internal list of dependents
   - Multiple observers can register with the same subject
   - Observers can also unregister using detach() method

5. **State Change Notification**: Subject notifies all observers when state changes.
   - Subject calls notify() method when its state changes
   - Notification is sent to all registered observers in the list
   - Each observer's update() method is called with relevant information
   - Observers can then query the subject for additional details if needed

6. **Observer Response**: Each observer processes the notification according to its needs.
   - Observer's update() method handles the notification
   - Observer can update its own state based on the subject's change
   - Multiple observers can respond differently to the same notification
   - Promotes loose coupling since subject doesn't know observer details

Example: News Publishing System
- Subject: NewsPublisher that publishes breaking news
- Observers: EmailSubscriber, SMSSubscriber that receive notifications
- Usage: When news is published, all subscribers are automatically notified

Benefits:
- Loose coupling between subject and observers
- Dynamic relationships - observers can be added/removed at runtime
- Broadcast communication - one-to-many notification
- Supports the Open/Closed Principle for adding new observer types

Common Use Cases:
- Model-View-Controller (MVC) architectures
- Event handling systems and GUI components
- Publish-Subscribe messaging patterns
- Real-time data updates and notifications
- Logging and monitoring systems

Drawbacks:
- Can cause memory leaks if observers are not properly detached
- Notification order is not guaranteed
- Can create complex update chains if observers modify the subject
- Debugging can be difficult due to indirect communication

This pattern demonstrates effective decoupling and is fundamental for
building flexible, event-driven systems with automatic state synchronization.
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
