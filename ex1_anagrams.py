from __future__ import annotations

from collections import Counter, defaultdict


def is_anagram_1(a: str, b: str) -> bool:
    """
    Determine if strings a and b are anagrams of each other by stepping through
    each character from a and removing a match from b. If b does not have a
    character, or has more characters left after finishing, the two strings are
    not anagrams.
    """
    for char in a:
        b_index = b.find(char)
        if b_index == -1:
            return False
        b = b[:b_index] + b[b_index + 1 :]
    return len(b) == 0


def is_anagram_2(a: str, b: str) -> bool:
    """
    Determine if strings a and b are anagrams by comparing the frequency counts
    of the characters in each.
    """
    a_counter: defaultdict[str, int] = defaultdict(int)
    for char in a:
        a_counter[char] += 1
    b_counter: defaultdict[str, int] = defaultdict(int)
    for char in b:
        b_counter[char] += 1
    return a_counter == b_counter


def is_anagram_3(a: str, b: str) -> bool:
    """
    Determine if strings a and b are anagrams by comparing the frequency counts
    of the characters in each.
    """
    return Counter(a) == Counter(b)
