"""
Singleton Design Pattern Explained Step-by-Step
----------------------------------------------
The Singleton Design Pattern is a creational design pattern that ensures a class has only one instance
and provides a global point of access to that instance. It restricts the instantiation of a class to
a single object, which is useful when exactly one object is needed to coordinate actions across the
system. This pattern is essential for managing shared resources like configuration settings, logging
systems, database connections, and caches where having multiple instances could cause conflicts or
waste resources.

Here is how the process works:

1. **Private Constructor**: Prevent direct instantiation of the class.
   - Constructor is typically made private or controlled through metaclass
   - Direct instantiation using `Class()` is restricted or controlled
   - Ensures clients cannot create multiple instances accidentally
   - Forces all access to go through the designated creation method

2. **Static Instance Variable**: Store the single instance as a class variable.
   - Class maintains a private static reference to the single instance
   - This variable holds the one and only instance of the class
   - Initialized to None or empty until first instance is created
   - Shared across all attempts to access the singleton

3. **Instance Creation Check**: Check if instance already exists before creating new one.
   - Before creating a new instance, check if one already exists
   - If instance exists, return the existing instance
   - If no instance exists, create the first (and only) instance
   - This ensures only one instance is ever created

4. **Global Access Point**: Provide a static method or property to access the instance.
   - Public method or property provides controlled access to the singleton
   - Method typically named `getInstance()` or similar
   - Returns the single instance, creating it if necessary
   - Ensures consistent access pattern across the application

5. **Thread Safety**: Ensure singleton works correctly in multi-threaded environments.
   - Implement proper locking mechanisms for thread safety
   - Prevent race conditions during instance creation
   - Use synchronization techniques like locks or atomic operations
   - Metaclass approach in Python naturally handles thread safety

6. **Lazy Initialization**: Create the instance only when first needed.
   - Instance is created on first access, not at class definition time
   - Improves application startup time and memory usage
   - Resources are allocated only when actually needed
   - Delays expensive initialization until required

Example: Configuration Manager
- Single instance manages all application configuration settings
- Prevents conflicts from multiple configuration objects
- Provides global access to settings throughout the application
- Ensures consistent configuration state across all components

Benefits:
- Guarantees single instance of critical system resources
- Provides global access point without using global variables
- Saves memory by preventing multiple instances
- Ensures consistent state across the application
- Lazy initialization improves performance

Common Use Cases:
- Configuration and settings management
- Logging systems and audit trails
- Database connection pools and managers
- Cache managers and registry objects
- Device drivers and hardware interfaces
- Application state managers

Drawbacks:
- Can make unit testing difficult due to global state
- May introduce tight coupling between classes
- Can be overused leading to disguised global variables
- Difficult to extend or subclass properly
- May create bottlenecks in multi-threaded applications

This pattern demonstrates controlled object creation and is fundamental for
managing shared resources and maintaining consistent global state in applications.
"""

import threading


class SingletonMeta(type):
    """
    A metaclass that creates a Singleton base type when called.
    """

    _instances = {}

    # NOTE:
    # The `_lock` variable is a threading.Lock() used to ensure thread safety during lazy initialization.
    # Without this lock, multiple threads could simultaneously enter the `__call__` method and create multiple instances.
    # Here's how it works:
    # - The first `if cls not in cls._instances` check avoids locking for performance in most cases.
    # - If the instance doesn't exist, we acquire the lock.
    # - Inside the locked block, we check again (`double-checked locking`) to ensure no other thread created the instance while we were waiting.
    # - This guarantees that only one instance is ever created, even in multi-threaded environments.
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # First check without locking for performance
        if cls not in cls._instances:
            with cls._lock:
                # Double-checked locking
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


# NOTE:
# The parameter `metaclass=SingletonMeta` tells Python to use the SingletonMeta class to construct ConfigurationManager.
# This means:
# - Instead of using the default `type` metaclass, Python delegates instance creation to SingletonMeta.
# - SingletonMeta overrides the `__call__` method to ensure only one instance of ConfigurationManager is ever created.
# - Any time you call ConfigurationManager(), it checks if an instance already exists and returns it if so.
# This is how the Singleton behavior is enforced without modifying the ConfigurationManager class itself.
class ConfigurationManager(metaclass=SingletonMeta):
    """
    Example Singleton class for managing configuration.
    """

    def __init__(self):
        self.settings = {}

    def set(self, key: str, value: str):
        self.settings[key] = value

    def get(self, key: str) -> str:
        return self.settings.get(key, "")
