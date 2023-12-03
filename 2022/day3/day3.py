"""Advent of Code 2022 Day 3."""

from itertools import batched
from string import ascii_letters

from advent_of_code.util import inputs


def _split_backpack(line: str) -> tuple[str, str]:
    """Splits a line into two - representing the two backpack comparments."""
    mid = int(len(line) / 2)
    return line[0:mid], line[mid:]


def _calculate_priority(first: str, second: str) -> int:
    """Calculates the shared item priority of two backpack compartments.

    Args:
        first (str): the first compartment string
        second (str): the second compartment string

    Returns:
        int: the score of the shared item
    """
    for item in first:
        if item not in second:
            continue
        break
    return ascii_letters.index(item) + 1


def _calculate_group_priority(first: str, second: str, third: str) -> int:
    """Calculates the shared item priority of three backpacks.

    Args:
        first (str): the first backpack string
        second (str): the second backpack string
        third (str): the third backpack string

    Returns:
        int: the score of the shared item
    """
    for item in first:
        if item in second and item in third:
            break
    return ascii_letters.index(item) + 1


if __name__ == "__main__":
    lines = inputs.get_input()

    # part one
    part_one_total = 0
    for line in lines:
        score = _calculate_priority(*_split_backpack(line))
        part_one_total += score
    print(part_one_total)

    # part two
    part_two_total = 0
    for group in batched(lines, 3):
        score = _calculate_group_priority(*group)
        part_two_total += score
    print(part_two_total)
