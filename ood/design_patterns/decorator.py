"""
Decorator Design Pattern Explained Step-by-Step
-----------------------------------------------
The Decorator Design Pattern is a structural design pattern that allows behavior to be added to
objects dynamically without altering their structure. This pattern is essential for extending
functionality in a flexible and modular way, avoiding the need for extensive subclassing.
It enables you to wrap objects with new behaviors while keeping the same interface, making it
perfect for adding features like logging, authentication, caching, or formatting to existing
objects without modifying their core implementation.

Here is how the process works:

1. **Component Interface**: Define the base interface that both concrete components and decorators will implement.
   - Abstract base class that declares the common operations
   - Ensures all components and decorators follow the same contract
   - Provides the foundation for consistent behavior across all implementations
   - Allows decorators and components to be used interchangeably

2. **Concrete Component**: Implement the base functionality without any decorations.
   - Provides the core implementation of the component interface
   - Contains the original behavior that can be enhanced by decorators
   - Serves as the base object that decorators will wrap
   - Represents the simplest form of the component

3. **Base Decorator**: Create an abstract decorator that holds a reference to a component.
   - Implements the component interface and contains a wrapped component
   - Provides default behavior by delegating calls to the wrapped component
   - Establishes the structure for concrete decorators to follow
   - Maintains the component reference for decorator chaining

4. **Concrete Decorators**: Implement specific decorations that add new behavior.
   - Extend the base decorator with additional functionality
   - Call the wrapped component's methods and add extra behavior before/after
   - Can modify input parameters or return values as needed
   - Multiple decorators can be chained together for complex behavior

5. **Object Wrapping**: Decorators wrap components or other decorators to create layered behavior.
   - Each decorator receives a component (or another decorator) in its constructor
   - Creates a chain of decorators where each adds its own behavior
   - Maintains the component interface throughout the decoration chain
   - Allows for flexible composition of behaviors at runtime

6. **Behavior Execution**: When a method is called, it propagates through the decorator chain.
   - The outermost decorator receives the method call first
   - Each decorator can add behavior before calling the wrapped component
   - The call eventually reaches the concrete component for core functionality
   - Return values can be modified by decorators as they propagate back

Example: Notification System
- Component: BasicNotifier that sends simple notifications
- Decorators: SMSDecorator, EmailDecorator, SlackDecorator for multiple channels
- Usage: Wrap basic notifier with multiple decorators for multi-channel notifications

Benefits:
- More flexible than static inheritance
- Adds responsibilities to objects dynamically
- Supports composition over inheritance principle
- Allows for multiple decorations and complex behavior combinations

Common Use Cases:
- Adding features to UI components (borders, scrollbars)
- Middleware in web frameworks
- Stream processing and data transformation
- Adding cross-cutting concerns (logging, security, caching)
- Enhancing existing APIs without modification

Drawbacks:
- Can create many small objects leading to complex object hierarchies
- Debugging can be difficult due to multiple layers of decoration
- Order of decoration matters and can affect behavior
- Can make the system harder to understand and maintain

This pattern demonstrates effective composition and is fundamental for
building flexible, extensible systems with modular behavior enhancement.
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
