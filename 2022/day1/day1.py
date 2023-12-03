"""Advent of code 2022 Day 1."""

from advent_of_code.util import inputs


def _calculate_calories(lines: list[str]) -> list[int]:
    """Calculates the calories for each elf.

    The amount of calories carried by a single elf is separted by an empty line.

    Args:
        lines (list[str]): the line

    Returns:
        list[int]: list of calculated calories
    """
    current = 0
    calories = []
    for line in lines:
        if not line:
            calories.append(current)
            current = 0
            continue
        current += int(line)
    return calories


if __name__ == "__main__":
    lines = inputs.get_input()
    calories = sorted(_calculate_calories(lines), reverse=True)
    # part one
    print(calories[0])
    # part two
    print(sum([calories[0], calories[1], calories[2]]))
