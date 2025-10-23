"""
Singleton Design Pattern
----------------------------------------------

It ensures that a class has only one instance and provides a global point of access to it.

- Intent: Restrict instantiation of a class to a single object.
- Use Case: Managing shared resources like configuration, logging, or database connections.
"""


class SingletonMeta(type):
    """
    A metaclass that creates a Singleton base type when called.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


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
