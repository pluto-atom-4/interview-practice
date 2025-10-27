"""
classic object-oriented pattern that lets you add behavior to objects dynamically without modifying their structure.
- Intent: Attach additional responsibilities to an object dynamically.
- Use Case: Logging, authentication, formatting, caching, or enhancing behavior without subclassing.
"""


from abc import ABC, abstractmethod


# Component Interface
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        pass

# Concrete Component
class BasicNotifier(Notifier):
    def send(self, message: str) -> str:
        return f"Basic Notification: {message}"

# Base Decorator
class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self._notifier = notifier

    def send(self, message: str) -> str:
        return self._notifier.send(message)

# Concrete Decorators
class SMSDecorator(NotifierDecorator):
    def send(self, message: str) -> str:
        base = super().send(message)
        return f"{base}\nSMS sent: {message}"

class EmailDecorator(NotifierDecorator):
    def send(self, message: str) -> str:
        base = super().send(message)
        return f"{base}\nEmail sent: {message}"

class SlackDecorator(NotifierDecorator):
    def send(self, message: str) -> str:
        base = super().send(message)
        return f"{base}\nSlack message sent: {message}"

# Utility function to visualize the decorator chain
def visualize_decorator_chain(notifier):
    """
    Prints the decorator chain from innermost to outermost.
    """
    chain = []
    current = notifier
    while hasattr(current, "_notifier"):
        chain.append(type(current).__name__)
        current = current._notifier
    chain.append(type(current).__name__)  # Add the base component

    print("Decorator Chain:")
    for i, name in enumerate(reversed(chain)):
        indent = "    " * i
        arrow = "└── " if i > 0 else ""
        print(f"{indent}{arrow}{name}")