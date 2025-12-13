from leetcode.trie_singledispatch import make_trie


def test_trie_singledispatch_basic():
    t = make_trie()
    t["insert"]("apple")

    assert t["search"]("apple") is True
    assert t["search"]("app") is False
    assert t["startsWith"]("app") is True

    t["insert"]("app")
    assert t["search"]("app") is True


def test_trie_singledispatch_empty():
    t = make_trie()
    assert t["search"]("") is False
    assert t["startsWith"]("") is True


def test_trie_singledispatch_multiple_words():
    t = make_trie()
    words = ["cat", "car", "cart", "dog"]

    for w in words:
        t["insert"](w)

    assert t["search"]("cat")
    assert t["search"]("car")
    assert t["search"]("cart")
    assert t["search"]("dog")

    assert not t["search"]("ca")
    assert t["startsWith"]("ca")
    assert t["startsWith"]("car")
    assert not t["startsWith"]("cow")
