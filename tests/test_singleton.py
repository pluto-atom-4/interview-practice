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
