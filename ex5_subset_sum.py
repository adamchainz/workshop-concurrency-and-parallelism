from __future__ import annotations

from itertools import combinations


def find_subset_sum(
    choices: set[int],
    target: int,
) -> set[int] | None:
    for subselection_size in range(1, len(choices) + 1):
        for subselection in combinations(choices, subselection_size):
            if sum(subselection) == target:
                return set(subselection)
    return None
