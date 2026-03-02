import pytest

from leetcode.trie_oop import Trie


def test_insert_and_search():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False  # not a full word yet


def test_starts_with():
    trie = Trie()
    trie.insert("apple")
    assert trie.starts_with("app") is True
    assert trie.starts_with("appl") is True
    assert trie.starts_with("banana") is False


def test_insert_prefix_then_word():
    trie = Trie()
    trie.insert("app")
    assert trie.search("app") is True
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.starts_with("app") is True


def test_multiple_words():
    trie = Trie()
    words = ["cat", "car", "cart", "dog", "dove"]
    for w in words:
        trie.insert(w)

    for w in words:
        assert trie.search(w) is True

    assert trie.search("do") is False
    assert trie.starts_with("do") is True
    assert trie.starts_with("ca") is True
    assert trie.starts_with("cow") is False


def test_empty_string_behavior():
    trie = Trie()
    trie.insert("")
    assert trie.search("") is True
    assert trie.starts_with("") is True
