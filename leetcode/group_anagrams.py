from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:

    groups = defaultdict(list)

    for word in strs:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord("a")] += 1
        groups[tuple(freq)].append(word)

    return list(groups.values())
