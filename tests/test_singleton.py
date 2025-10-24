import threading

import pytest

from ood.design_patterns.singleton import ConfigurationManager


def test_singleton_identity():
    config1 = ConfigurationManager()
    config2 = ConfigurationManager()
    assert config1 is config2  # Both should be the same instance


def test_singleton_data_persistence():
    config = ConfigurationManager()
    config.set("env", "production")
    assert config.get("env") == "production"

    # Access from another reference
    another_config = ConfigurationManager()
    assert another_config.get("env") == "production"


def test_thread_safe_singleton():
    instances = []

    def create_instance():
        instances.append(ConfigurationManager())

    threads = [threading.Thread(target=create_instance) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # All instances should be the same
    assert all(inst is instances[0] for inst in instances)
