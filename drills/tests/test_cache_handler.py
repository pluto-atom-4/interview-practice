import pytest
import time
from unittest.mock import patch
from drills.cache_handler import CacheHandler


class TestCacheHandlerBasicOperations:
    """Test basic PUT, GET, DELETE operations."""

    def test_put_without_duration(self):
        """PUT should return ACCEPTED and store value without expiration."""
        cache = CacheHandler()
        result = cache.put("key1", "value1")
        assert result == "ACCEPTED"
        assert cache.get("key1") == "value1"

    def test_put_with_duration(self):
        """PUT with duration should return ACCEPTED and store value with TTL."""
        cache = CacheHandler()
        result = cache.put("key1", "value1", 5000)
        assert result == "ACCEPTED"
        assert cache.get("key1") == "value1"

    def test_get_nonexistent_key(self):
        """GET on non-existent key should return NOT FOUND."""
        cache = CacheHandler()
        assert cache.get("nonexistent") == "NOT FOUND"

    def test_get_existing_key(self):
        """GET on existing key should return its value."""
        cache = CacheHandler()
        cache.put("key1", "value1")
        assert cache.get("key1") == "value1"

    def test_delete_existing_key(self):
        """DELETE on existing key should return ACCEPTED and remove it."""
        cache = CacheHandler()
        cache.put("key1", "value1")
        assert cache.delete("key1") == "ACCEPTED"
        assert cache.get("key1") == "NOT FOUND"

    def test_delete_nonexistent_key(self):
        """DELETE on non-existent key should return NOT FOUND."""
        cache = CacheHandler()
        assert cache.delete("nonexistent") == "NOT FOUND"

    def test_put_overwrites_existing_key(self):
        """PUT should overwrite existing key value."""
        cache = CacheHandler()
        cache.put("key1", "value1")
        cache.put("key1", "value2")
        assert cache.get("key1") == "value2"

    def test_put_updates_ttl(self):
        """PUT on existing key should update its TTL."""
        cache = CacheHandler()
        cache.put("key1", "value1", 10000)
        cache.put("key1", "value1", 5000)  # Update TTL
        assert cache.get("key1") == "value1"


class TestCacheHandlerExpiration:
    """Test TTL and expiration functionality."""

    def test_get_expired_key(self):
        """GET on expired key should return NOT FOUND and cleanup."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("key1", "value1", 1000)  # expires at 1000ms

        # Advance time past expiration
        with patch('time.time', return_value=2):  # 2000ms > 1000ms
            result = cache.get("key1")
            assert result == "NOT FOUND"
            assert "key1" not in cache.store

    def test_delete_expired_key(self):
        """DELETE on expired key should return NOT FOUND and cleanup."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("key1", "value1", 1000)

        with patch('time.time', return_value=2):  # 2000ms > 1000ms
            result = cache.delete("key1")
            assert result == "NOT FOUND"
            assert "key1" not in cache.store

    def test_patch_expired_key(self):
        """PATCH on expired key should return NOT FOUND."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("key1", "value1", 1000)

        with patch('time.time', return_value=2):  # 2000ms > 1000ms
            result = cache.patch("key1", 5000)
            assert result == "NOT FOUND"

    def test_key_still_valid_before_expiration(self):
        """GET should return value before TTL expires."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("key1", "value1", 2000)  # expires at 2000ms

        with patch('time.time', return_value=1):  # 1000ms < 2000ms
            assert cache.get("key1") == "value1"

    def test_key_expired_at_exact_expiration_time(self):
        """GET should return NOT FOUND at exact expiration timestamp."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("key1", "value1", 1000)  # expires at 1000ms

        with patch('time.time', return_value=1):  # 1000ms (exactly at expiration)
            result = cache.get("key1")
            assert result == "NOT FOUND"

    def test_no_expiration_key_persists(self):
        """Key without TTL should persist indefinitely."""
        cache = CacheHandler()
        cache.put("key1", "value1")  # No duration

        with patch('time.time', return_value=100):  # Simulate time passing
            assert cache.get("key1") == "value1"


class TestCacheHandlerPatch:
    """Test PATCH operation for updating TTL."""

    def test_patch_existing_key(self):
        """PATCH should update TTL on existing key."""
        cache = CacheHandler()
        cache.put("key1", "value1", 1000)
        result = cache.patch("key1", 5000)
        assert result == "ACCEPTED"
        assert cache.get("key1") == "value1"

    def test_patch_nonexistent_key(self):
        """PATCH on non-existent key should return NOT FOUND."""
        cache = CacheHandler()
        result = cache.patch("nonexistent", 5000)
        assert result == "NOT FOUND"

    def test_patch_extends_expiration(self):
        """PATCH should extend TTL of key."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("key1", "value1", 1000)  # expires at 1000ms

        with patch('time.time', return_value=0.5):  # 500ms
            cache.patch("key1", 1500)  # Extend to 500 + 1500 = 2000ms

        with patch('time.time', return_value=1):  # 1000ms
            assert cache.get("key1") == "value1"  # Still valid

    def test_patch_shortens_expiration(self):
        """PATCH should be able to shorten TTL."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("key1", "value1", 5000)

        with patch('time.time', return_value=0):
            cache.patch("key1", 500)  # Shorten to 500ms

        with patch('time.time', return_value=1):  # 1000ms > 500ms
            assert cache.get("key1") == "NOT FOUND"

    def test_patch_key_without_ttl(self):
        """PATCH should add TTL to key that has no expiration."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("key1", "value1")  # No TTL
            result = cache.patch("key1", 1000)  # Set TTL at time 0
            assert result == "ACCEPTED"
            assert cache.get("key1") == "value1"

        with patch('time.time', return_value=2):  # Past 1000ms expiration
            assert cache.get("key1") == "NOT FOUND"


class TestCacheHandlerCount:
    """Test count() functionality."""

    def test_count_empty_cache(self):
        """count() on empty cache should return 0."""
        cache = CacheHandler()
        assert cache.count() == 0

    def test_count_single_key(self):
        """count() should return 1 for single key."""
        cache = CacheHandler()
        cache.put("key1", "value1")
        assert cache.count() == 1

    def test_count_multiple_keys(self):
        """count() should return number of stored keys."""
        cache = CacheHandler()
        cache.put("key1", "value1")
        cache.put("key2", "value2")
        cache.put("key3", "value3")
        assert cache.count() == 3

    def test_count_excludes_expired_keys(self):
        """count() should exclude expired keys and cleanup."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("key1", "value1", 1000)
            cache.put("key2", "value2", 1000)
            cache.put("key3", "value3")  # No expiration
            assert cache.count() == 3

        with patch('time.time', return_value=2):  # 2000ms, past expiration
            count = cache.count()
            assert count == 1  # Only key3
            assert "key1" not in cache.store
            assert "key2" not in cache.store

    def test_count_with_mixed_ttl_keys(self):
        """count() should handle mix of TTL and non-TTL keys."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("key1", "value1", 1000)
            cache.put("key2", "value2")  # No TTL
            cache.put("key3", "value3", 2000)

        with patch('time.time', return_value=1.5):  # 1500ms
            count = cache.count()
            assert count == 2  # key2 and key3


class TestCacheHandlerExecute:
    """Test batch command execution."""

    def test_execute_put_command(self):
        """execute() should handle PUT command."""
        cache = CacheHandler()
        results = cache.execute(["PUT key1 value1"])
        assert results == ["ACCEPTED"]
        assert cache.get("key1") == "value1"

    def test_execute_put_with_duration(self):
        """execute() should handle PUT with duration."""
        cache = CacheHandler()
        results = cache.execute(["PUT key1 value1 5000"])
        assert results == ["ACCEPTED"]
        assert cache.get("key1") == "value1"

    def test_execute_get_command(self):
        """execute() should handle GET command."""
        cache = CacheHandler()
        cache.put("key1", "value1")
        results = cache.execute(["GET key1"])
        assert results == ["value1"]

    def test_execute_get_nonexistent(self):
        """execute() should return NOT FOUND for GET on missing key."""
        cache = CacheHandler()
        results = cache.execute(["GET nonexistent"])
        assert results == ["NOT FOUND"]

    def test_execute_delete_command(self):
        """execute() should handle DELETE command."""
        cache = CacheHandler()
        cache.put("key1", "value1")
        results = cache.execute(["DELETE key1"])
        assert results == ["ACCEPTED"]
        assert cache.get("key1") == "NOT FOUND"

    def test_execute_delete_nonexistent(self):
        """execute() should return NOT FOUND for DELETE on missing key."""
        cache = CacheHandler()
        results = cache.execute(["DELETE nonexistent"])
        assert results == ["NOT FOUND"]

    def test_execute_patch_command(self):
        """execute() should handle PATCH command."""
        cache = CacheHandler()
        cache.put("key1", "value1", 5000)
        results = cache.execute(["PATCH key1 TTL=10000"])
        assert results == ["ACCEPTED"]

    def test_execute_patch_nonexistent(self):
        """execute() should return NOT FOUND for PATCH on missing key."""
        cache = CacheHandler()
        results = cache.execute(["PATCH nonexistent TTL=5000"])
        assert results == ["NOT FOUND"]

    def test_execute_multiple_commands(self):
        """execute() should process multiple commands in sequence."""
        cache = CacheHandler()
        commands = [
            "PUT key1 value1",
            "PUT key2 value2 5000",
            "GET key1",
            "GET key2",
            "DELETE key1",
            "GET key1"
        ]
        results = cache.execute(commands)
        assert results == [
            "ACCEPTED",
            "ACCEPTED",
            "value1",
            "value2",
            "ACCEPTED",
            "NOT FOUND"
        ]

    def test_execute_complex_workflow(self):
        """execute() should handle complex workflow with PATCH."""
        cache = CacheHandler()
        commands = [
            "PUT a 10",
            "GET a",
            "PATCH a TTL=5000",
            "GET a",
            "DELETE a",
            "GET a"
        ]
        results = cache.execute(commands)
        assert results == [
            "ACCEPTED",
            "10",
            "ACCEPTED",
            "10",
            "ACCEPTED",
            "NOT FOUND"
        ]

    def test_execute_case_insensitive_commands(self):
        """execute() should handle commands case-insensitively."""
        cache = CacheHandler()
        results = cache.execute([
            "put key1 value1",
            "get key1",
            "delete key1",
            "get key1"
        ])
        assert results == ["ACCEPTED", "value1", "ACCEPTED", "NOT FOUND"]

    def test_execute_invalid_put_command(self):
        """execute() should return error for invalid PUT."""
        cache = CacheHandler()
        results = cache.execute(["PUT key1"])  # Missing value
        assert results == ["INVALID COMMAND"]

    def test_execute_invalid_duration(self):
        """execute() should return error for non-integer duration."""
        cache = CacheHandler()
        results = cache.execute(["PUT key1 value1 notanumber"])
        assert results == ["INVALID DURATION"]

    def test_execute_invalid_ttl_format(self):
        """execute() should return error for invalid TTL format."""
        cache = CacheHandler()
        cache.put("key1", "value1")
        results = cache.execute(["PATCH key1 DURATION=5000"])  # Wrong format
        assert results == ["INVALID TTL FORMAT"]

    def test_execute_invalid_ttl_value(self):
        """execute() should return error for non-integer TTL value."""
        cache = CacheHandler()
        cache.put("key1", "value1")
        results = cache.execute(["PATCH key1 TTL=notanumber"])
        assert results == ["INVALID TTL VALUE"]

    def test_execute_unknown_command(self):
        """execute() should return error for unknown command."""
        cache = CacheHandler()
        results = cache.execute(["UNKNOWN key1"])
        assert results == ["UNKNOWN COMMAND"]

    def test_execute_empty_commands(self):
        """execute() should handle empty command list."""
        cache = CacheHandler()
        results = cache.execute([])
        assert results == []

    def test_execute_empty_string_command(self):
        """execute() should skip empty string commands."""
        cache = CacheHandler()
        results = cache.execute(["", "PUT key1 value1", ""])
        assert results == ["ACCEPTED"]


class TestCacheHandlerIntegration:
    """Integration tests combining multiple features."""

    def test_multiple_keys_with_different_ttls(self):
        """Test managing multiple keys with different TTLs."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("short", "value1", 500)
            cache.put("medium", "value2", 1500)
            cache.put("long", "value3", 3000)
            cache.put("infinite", "value4")  # No TTL

        # At 1000ms
        with patch('time.time', return_value=1):
            assert cache.get("short") == "NOT FOUND"
            assert cache.get("medium") == "value2"
            assert cache.get("long") == "value3"
            assert cache.get("infinite") == "value4"
            assert cache.count() == 3

    def test_patch_after_partial_expiration(self):
        """Test PATCH updating TTL of surviving keys."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("key1", "value1", 1000)
            cache.put("key2", "value2", 1000)

        with patch('time.time', return_value=0.5):
            cache.patch("key2", 1500)  # Extend key2

        with patch('time.time', return_value=1.2):  # 1200ms
            assert cache.get("key1") == "NOT FOUND"
            assert cache.get("key2") == "value2"  # Still valid due to patch

    def test_workflow_with_overwrites(self):
        """Test workflow with key overwrites and TTL changes."""
        cache = CacheHandler()
        commands = [
            "PUT key1 value1 1000",
            "PUT key1 value2",  # Overwrite without TTL
            "GET key1"
        ]
        results = cache.execute(commands)
        assert results == ["ACCEPTED", "ACCEPTED", "value2"]

        # key1 should now have no expiration
        with patch('time.time', return_value=10):
            assert cache.get("key1") == "value2"

    def test_rapid_operations_same_key(self):
        """Test rapid PUT/PATCH operations on same key."""
        cache = CacheHandler()
        commands = [
            "PUT key TTL1 5000",
            "PATCH key TTL=10000",
            "GET key",
            "PATCH key TTL=1000",
            "GET key"
        ]
        results = cache.execute(commands)
        assert results == ["ACCEPTED", "ACCEPTED", "TTL1", "ACCEPTED", "TTL1"]

    def test_large_batch_operations(self):
        """Test large batch of operations."""
        cache = CacheHandler()
        commands = []
        for i in range(10):
            commands.append(f"PUT key{i} value{i} 5000")
        for i in range(10):
            commands.append(f"GET key{i}")

        results = cache.execute(commands)
        assert results[:10] == ["ACCEPTED"] * 10
        assert results[10:] == [f"value{i}" for i in range(10)]

    def test_delete_then_readd_same_key(self):
        """Test deleting and re-adding the same key."""
        cache = CacheHandler()
        commands = [
            "PUT key1 value1",
            "DELETE key1",
            "GET key1",
            "PUT key1 newvalue",
            "GET key1"
        ]
        results = cache.execute(commands)
        assert results == ["ACCEPTED", "ACCEPTED", "NOT FOUND", "ACCEPTED", "newvalue"]


class TestCacheHandlerEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_very_small_ttl(self):
        """Test with very small TTL value."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("key1", "value1", 1)  # 1ms TTL

        with patch('time.time', return_value=0.002):  # 2ms
            assert cache.get("key1") == "NOT FOUND"

    def test_very_large_ttl(self):
        """Test with very large TTL value."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("key1", "value1", 10000000)  # Very large TTL

        with patch('time.time', return_value=1000):  # 1000 seconds (plenty within TTL)
            assert cache.get("key1") == "value1"

    def test_zero_ttl(self):
        """Test with zero TTL (expires immediately)."""
        cache = CacheHandler()
        with patch('time.time', return_value=0):
            cache.put("key1", "value1", 0)

        with patch('time.time', return_value=0):
            assert cache.get("key1") == "NOT FOUND"

    def test_special_characters_in_values(self):
        """Test values with special characters."""
        cache = CacheHandler()
        # Note: Command parsing uses split(), so multi-word values aren't supported
        cache.put("key1", "value123!@#")
        assert cache.get("key1") == "value123!@#"

    def test_numeric_string_values(self):
        """Test storing numeric strings as values."""
        cache = CacheHandler()
        cache.put("count", "42")
        assert cache.get("count") == "42"

    def test_key_with_numbers(self):
        """Test keys with numbers."""
        cache = CacheHandler()
        cache.put("key123", "value")
        assert cache.get("key123") == "value"

    def test_single_character_key(self):
        """Test single character key."""
        cache = CacheHandler()
        cache.put("a", "value")
        assert cache.get("a") == "value"
        assert cache.count() == 1

    def test_unicode_key_and_value(self):
        """Test unicode in keys and values."""
        cache = CacheHandler()
        cache.put("键", "值")
        assert cache.get("键") == "值"

    def test_count_after_various_operations(self):
        """Test count() accuracy after various operations."""
        cache = CacheHandler()
        assert cache.count() == 0

        cache.put("k1", "v1")
        assert cache.count() == 1

        cache.put("k2", "v2")
        assert cache.count() == 2

        cache.delete("k1")
        assert cache.count() == 1

        cache.put("k1", "v1_new")
        assert cache.count() == 2


class TestCacheHandlerWhitespaceNormalization:
    """Test whitespace normalization in command parsing."""

    def test_execute_extra_spaces_between_tokens(self):
        """execute() should handle extra spaces between command tokens."""
        cache = CacheHandler()
        results = cache.execute(["PUT   key1   value1"])
        assert results == ["ACCEPTED"]
        assert cache.get("key1") == "value1"

    def test_execute_extra_spaces_in_get(self):
        """execute() should handle extra spaces in GET command."""
        cache = CacheHandler()
        cache.put("key1", "value1")
        results = cache.execute(["GET    key1"])
        assert results == ["value1"]

    def test_execute_extra_spaces_in_delete(self):
        """execute() should handle extra spaces in DELETE command."""
        cache = CacheHandler()
        cache.put("key1", "value1")
        results = cache.execute(["DELETE    key1"])
        assert results == ["ACCEPTED"]
        assert cache.get("key1") == "NOT FOUND"

    def test_execute_extra_spaces_in_patch(self):
        """execute() should handle extra spaces in PATCH command."""
        cache = CacheHandler()
        cache.put("key1", "value1", 5000)
        results = cache.execute(["PATCH   key1   TTL=10000"])
        assert results == ["ACCEPTED"]
        assert cache.get("key1") == "value1"

    def test_execute_extra_spaces_with_duration(self):
        """execute() should handle extra spaces with PUT duration."""
        cache = CacheHandler()
        results = cache.execute(["PUT   key1   value1   5000"])
        assert results == ["ACCEPTED"]
        assert cache.get("key1") == "value1"

    def test_execute_leading_trailing_spaces_in_command(self):
        """execute() should handle leading/trailing spaces in command."""
        cache = CacheHandler()
        # Note: The user may strip leading/trailing spaces before split(),
        # or split() naturally handles them (it removes all leading/trailing)
        results = cache.execute(["  PUT key1 value1  "])
        assert results == ["ACCEPTED"]
        assert cache.get("key1") == "value1"

    def test_execute_tabs_as_whitespace(self):
        """execute() should treat tabs as whitespace."""
        cache = CacheHandler()
        results = cache.execute(["PUT\tkey1\tvalue1"])
        assert results == ["ACCEPTED"]
        assert cache.get("key1") == "value1"

    def test_execute_mixed_spaces_and_tabs(self):
        """execute() should handle mixed spaces and tabs."""
        cache = CacheHandler()
        results = cache.execute(["PUT  \t key1 \t value1"])
        assert results == ["ACCEPTED"]
        assert cache.get("key1") == "value1"

    def test_execute_whitespace_in_multiple_commands(self):
        """execute() should normalize whitespace in all commands."""
        cache = CacheHandler()
        commands = [
            "PUT   key1   value1",
            "GET  key1",
            "PATCH   key1   TTL=5000",
            "DELETE    key1"
        ]
        results = cache.execute(commands)
        assert results == ["ACCEPTED", "value1", "ACCEPTED", "ACCEPTED"]

    def test_execute_whitespace_with_invalid_commands(self):
        """execute() should still detect invalid commands with extra whitespace."""
        cache = CacheHandler()
        results = cache.execute(["PUT   key1"])  # Missing value, even with extra spaces
        assert results == ["INVALID COMMAND"]

    def test_execute_whitespace_preserves_key_value_identity(self):
        """Whitespace normalization should not affect key/value content."""
        cache = CacheHandler()
        cache.execute(["PUT key123 valueABC"])
        # Should be able to retrieve with exact key
        results = cache.execute(["GET key123"])
        assert results == ["valueABC"]

