"""Advent of Code 2022 Day 4."""

from advent_of_code.util import inputs


def _rangify_section(section: str) -> list[int]:
    """Turn a 'section' into a list of integers.

    Args:
        section (str): two numbers separted by a '-' as a string

    Returns:
        list[int]: the range of integers for the section
    """
    start, end = section.split("-")
    return list(range(int(start), int(end) + 1))


def _rangify_line(line: str) -> list[list[int], list[int]]:
    """Turns a line with two sections into two list of integers.

    Args:
        line (str): the line to process

    Returns:
        list[list[int], list[int]]: a list of two lists containing integers
    """
    first, second = line.split(",")
    return [_rangify_section(first), _rangify_section(second)]


def _check_total_containment(shorter: list[int], longer: list[int]) -> bool:
    """Checks if the entirety of the shorter list is contained within the longer list.

    Args:
        shorter (list[int]): a smaller list of integers
        longer (list[int]): a longer list of integers

    Returns:
        bool: whether the shorter is container within the longer
    """
    return all(x in longer for x in shorter)


def _check_any_containment(shorter: list[int], longer: list[int]) -> bool:
    """Checks if any items of the shorter list are also within the longer list.

    Args:
        shorter (list[int]): a smaller list of integers
        longer (list[int]): a longer list of integers

    Returns:
        bool: whether any of the items in shorter are container in longer
    """
    return any(x in longer for x in shorter)


if __name__ == "__main__":
    lines = inputs.get_input()

    # part one
    total = 0
    for line in lines:
        ranges = _rangify_line(line)
        if _check_total_containment(*sorted(ranges, key=len)):
            total += 1
    print(total)

    # part two
    total = 0
    for line in lines:
        ranges = _rangify_line(line)
        if _check_any_containment(*sorted(ranges, key=len)):
            total += 1
    print(total)
