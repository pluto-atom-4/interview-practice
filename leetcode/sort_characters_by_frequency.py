from collections import Counter


def frequency_sort(s: str) -> str:
    freq = Counter(s)
    # Descending sort by frequency
    sorted_chars = sorted(freq.items(), key=lambda x: -x[1])

    return "".join(ch * count for ch, count in sorted_chars)
