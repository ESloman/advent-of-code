"""Advent of Code 2023 Day 9."""

from itertools import pairwise
from operator import add, sub

from advent_of_code.util import inputs


def _get_next_sequence_item(seq: list[int], backwards: bool = False) -> int:
    """Gets the next item in the sequence.

    Args:
        seq (list[int]): the sequence of integers to find the next item for
        backwards (bool, optional): Whether to find the _previous_ item in the sequence. \
            Defaults to False.

    Returns:
        int: the next time
    """
    if set(seq) == {0}:
        return 0

    idx = -1 if not backwards else 0
    op = add if not backwards else sub

    difference = [b - a for a, b in pairwise(seq)]
    value = _get_next_sequence_item(difference, backwards)
    return op(seq[idx], value)


if __name__ == "__main__":
    lines = inputs.get_input()

    part_one_totals = 0
    part_two_totals = 0
    for line in lines:
        sequence = [int(ln) for ln in line.split()]
        part_one_totals += _get_next_sequence_item(sequence, False)
        part_two_totals += _get_next_sequence_item(sequence, True)
    print(part_one_totals, part_two_totals)
