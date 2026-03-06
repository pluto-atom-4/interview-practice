
import time
import pytest

from leetcode.cache_with_time_limit import TimeLimitedCache

def test_set_and_get_basic():
    cache = TimeLimitedCache()
    assert cache.set(1, 42, 1000) is False
    assert cache.get(1) == 42