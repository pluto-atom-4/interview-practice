
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class TrieNode:
    children: Dict[str, "TrieNode"] = field(default_factory=dict)
    is_end: bool = False


class Trie:
    def __init__(self)-> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end =True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node.is_end if node else False

    def starts_with(self, prefix: str)-> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, s: str) -> TrieNode | None :
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

