from __future__ import annotations


def add_numbers(a: int, b: int) -> int:
    return a + b
    # TODO: time complexity is: O(_)


def add_lists(a: list[int], b: list[int]) -> list[int]:
    return a + b
    # TODO: time complexity is O(_)
    # where n = total length of lists a and b


def unique_items(items: list[int]) -> list[int]:
    unique: list[int] = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique
    # TODO: time complexity is O(_)
    # where n = length of list items


def unique_items_with_set(items: list[int]) -> list[int]:
    unique: set[int] = set()
    for item in items:
        unique.add(item)
    return list(unique)
    # TODO: time complexity is O(_)
    # where n = length of list items
