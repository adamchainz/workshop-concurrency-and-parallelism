from __future__ import annotations

from ex1_anagrams import is_anagram_1, is_anagram_2, is_anagram_3


class BaseTestAnagram:
    def is_anagram(self, a: str, b: str) -> bool:
        raise NotImplementedError("Should be replaced in subclasses")

    def test_empty(self) -> None:
        assert self.is_anagram("", "")

    def test_single_character(self) -> None:
        assert self.is_anagram("!", "!")

    def test_multiple_same_characters(self) -> None:
        assert self.is_anagram("!!!", "!!!")

    def test_simple(self) -> None:
        assert self.is_anagram("door", "rood")

    def test_complex(self) -> None:
        assert self.is_anagram("the morse code", "here come dots")


class TestIsAnagram1(BaseTestAnagram):
    def is_anagram(self, a: str, b: str) -> bool:
        return is_anagram_1(a, b)


class TestIsAnagram2(BaseTestAnagram):
    def is_anagram(self, a: str, b: str) -> bool:
        return is_anagram_2(a, b)


class TestIsAnagram3(BaseTestAnagram):
    def is_anagram(self, a: str, b: str) -> bool:
        return is_anagram_3(a, b)
