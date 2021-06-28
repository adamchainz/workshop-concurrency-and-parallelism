from __future__ import annotations


def add_numbers(a: int, b: int) -> int:
    # TODO: time complexity is _
    # where n = total number of bits in a and b
    return a + b


def add_lists(a: list[int], b: list[int]) -> list[int]:
    # TODO: time complexity is _
    # where n = total length of lists a and b
    return a + b


def unique_items(input_: list[int]) -> list[int]:
    # TODO: time complexity is _
    # where n = length of list input_
    unique: list[int] = []
    for item in input_:
        if item not in unique:
            unique.append(item)
    return unique


def unique_items_with_set(input_: list[int]) -> list[int]:
    # TODO: time complexity is _
    # where n = length of list input_
    unique: set[int] = set()
    for item in input_:
        unique.add(item)
    return list(unique)
