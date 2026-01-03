import re


def is_valid_parentheses_regex(s: str) -> bool:
    """
    Regex-based implementation:
    Repeatedly remove valid '()', '[]', '{}' pairs until no more can be removed.
    If the string becomes empty, it's valid.
    """

    # Reject invalid characters early
    if re.search(r"[^()\[\]{}]", s):
        return False

    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"\(\)|\[]|{}", "", s)

    return s == ""
