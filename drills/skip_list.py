from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Any, Iterable, List, Optional, Tuple


@dataclass
class SkipListNode:
    score: float
    member: Any
    forwards: List[Optional["SkipListNode"]] = field(default_factory=list)


class SkipList:
    """
    Redis-like skip list for sorted sets:
    - Ordered by (score, member)
    - Supports insert, search, delete, range queries
    """

    def __init__(self, max_level: int = 16, p: float = 0.5):
        self.max_level = max_level
        self.p = p
        self.header = SkipListNode(score=float("-inf"), member=None,
                                   forwards=[None] * max_level)
        self.level = 0
        self.length = 0

    def _random_level(self) -> int:
        lvl = 0
        while random.random() < self.p and lvl < self.max_level - 1:
            lvl += 1
        return lvl

    def insert(self, member: Any, score: float) -> None:
        update: List[SkipListNode] = [self.header] * self.max_level
        current = self.header

        # Find update path
        for i in reversed(range(self.level + 1)):
            while (current.forwards[i] and
                   (current.forwards[i].score < score or
                    (current.forwards[i].score == score and
                     current.forwards[i].member < member))):
                current = current.forwards[i]
            update[i] = current

        # Check if member already exists (update score)
        candidate = current.forwards[0]
        if candidate and candidate.member == member:
            candidate.score = score
            return

        lvl = self._random_level()
        if lvl > self.level:
            for i in range(self.level + 1, lvl + 1):
                update[i] = self.header
            self.level = lvl

        new_node = SkipListNode(score=score, member=member,
                                forwards=[None] * (lvl + 1))

        for i in range(lvl + 1):
            new_node.forwards[i] = update[i].forwards[i]
            update[i].forwards[i] = new_node

        self.length += 1

    def search(self, member: Any) -> Optional[float]:
        current = self.header
        for i in reversed(range(self.level + 1)):
            while (current.forwards[i] and
                   current.forwards[i].member is not None and
                   current.forwards[i].member < member):
                current = current.forwards[i]

        current = current.forwards[0]
        if current and current.member == member:
            return current.score
        return None

    def remove(self, member: Any) -> bool:
        update: List[SkipListNode] = [self.header] * self.max_level
        current = self.header

        for i in reversed(range(self.level + 1)):
            while (current.forwards[i] and
                   current.forwards[i].member is not None and
                   current.forwards[i].member < member):
                current = current.forwards[i]
            update[i] = current

        target = current.forwards[0]
        if not target or target.member != member:
            return False

        for i in range(self.level + 1):
            if update[i].forwards[i] is target:
                update[i].forwards[i] = target.forwards[i]

        while self.level > 0 and self.header.forwards[self.level] is None:
            self.level -= 1

        self.length -= 1
        return True

    def range_by_score(self, min_score: float, max_score: float) -> Iterable[Tuple[Any, float]]:
        current = self.header

        # Move to first node with score >= min_score
        for i in reversed(range(self.level + 1)):
            while (current.forwards[i] and
                   current.forwards[i].score < min_score):
                current = current.forwards[i]

        current = current.forwards[0]
        while current and current.score <= max_score:
            yield current.member, current.score
            current = current.forwards[0]

    def __len__(self) -> int:
        return self.length

    def __iter__(self):
        node = self.header.forwards[0]
        while node:
            yield node.member, node.score
            node = node.forwards[0]
