"""
Strategy Design Pattern Explained Step-by-Step
----------------------------------------------
The Strategy Design Pattern is a behavioral design pattern that defines a family of algorithms,
encapsulates each one, and makes them interchangeable. It allows the algorithm to vary independently
from clients that use it. This pattern is essential for avoiding conditional statements and creating
flexible, maintainable code. It's commonly used in payment processing, sorting algorithms, validation
strategies, and any scenario where multiple approaches exist for solving the same problem.

Here is how the process works:

1. **Strategy Interface**: Define a common interface that all concrete strategies must implement.
   - Abstract base class or interface with abstract methods
   - Declares the algorithm interface that all strategies will follow
   - Ensures all concrete strategies have consistent method signatures
   - Provides the contract that context class depends on

2. **Concrete Strategies**: Implement different algorithms using the strategy interface.
   - Each class represents a specific algorithm or behavior variant
   - Implements the strategy interface with its own unique logic
   - Encapsulates the algorithm details within the strategy class
   - Can have different internal implementations while maintaining same interface

3. **Context Class**: Maintains a reference to a strategy object and delegates work to it.
   - Holds a reference to the current strategy instance
   - Provides methods to set/change the strategy at runtime
   - Delegates algorithm execution to the strategy object
   - Remains independent of specific algorithm implementations

4. **Strategy Selection**: Client code chooses which strategy to use.
   - Context can be initialized with a specific strategy
   - Strategy can be changed dynamically during runtime
   - Client decides which algorithm is appropriate for the situation
   - Enables flexible behavior modification without changing context code

5. **Algorithm Execution**: Context delegates the work to the selected strategy.
   - Context calls the strategy's methods when algorithm execution is needed
   - Strategy performs the actual work using its specific implementation
   - Results are returned through the common interface
   - Context remains unaware of the specific algorithm details

6. **Runtime Flexibility**: Strategies can be swapped without modifying the context.
   - New strategies can be added without changing existing code
   - Algorithms can be selected based on runtime conditions
   - Promotes Open/Closed Principle (open for extension, closed for modification)
   - Eliminates complex conditional logic in the context class

Example: Payment Processing System
- Strategies: CreditCardPayment, PayPalPayment, BitcoinPayment
- Context: PaymentProcessor that accepts any payment strategy
- Usage: Processor can switch between payment methods dynamically
- Benefit: Adding new payment methods doesn't require modifying existing code

Benefits:
- Eliminates conditional statements and switch cases
- Makes algorithms interchangeable at runtime
- Promotes code reusability and maintainability
- Follows Single Responsibility and Open/Closed principles
- Simplifies unit testing by isolating algorithm logic

Common Use Cases:
- Payment processing systems with multiple payment methods
- Sorting algorithms (QuickSort, MergeSort, BubbleSort)
- Validation strategies for different data types
- Compression algorithms (ZIP, RAR, TAR)
- Authentication methods (OAuth, LDAP, Database)

This pattern demonstrates object-oriented design principles and is fundamental for
creating flexible, extensible systems that can adapt to changing requirements.
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
