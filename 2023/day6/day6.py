"""Advent of Code 2023 Day 6."""

import math

from advent_of_code.util import inputs


def _get_times(line: str) -> list[int]:
    """Gets the times from the line.

    Args:
        line (str): the line

    Returns:
        list[int]: list of times
    """
    return [int(pt) for pt in line[5:].split(" ") if pt]


def _get_distances(line: str) -> list[int]:
    """Gets the distances from the line.

    Args:
        line (str): the line

    Returns:
        list[int]: list of distances
    """
    return [int(pt) for pt in line[9:].split(" ") if pt]


def _get_winning_times(time: int, distance: int) -> list[int]:
    """Gets the winning times.

    Args:
        time (int): the time
        distance (int): the record distance

    Returns:
        list[int]: list of winning times
    """
    return [hold_time for hold_time in range(1, time - 1) if _check_winning_time(time, distance, hold_time)]


def _check_winning_time(time: int, distance: int, hold_time: int) -> bool:
    """Checks a given time is a winning time.

    Args:
        time (int): the time
        distance (int): the record distance to beat
        hold_time (int): the hold time to check

    Returns:
        bool: whether this hold time can beat the record or not
    """
    return hold_time * (time - hold_time) > distance


if __name__ == "__main__":
    lines = inputs.get_input()

    # part one
    times = _get_times(lines[0])
    distances = _get_distances(lines[1])
    print(math.prod(len(_get_winning_times(*race)) for race in zip(times, distances, strict=True)))

    # part two
    # make it all one time
    time = int("".join(str(t) for t in times))
    distance = int("".join(str(d) for d in distances))

    lowest = None
    # find lowest
    for x in range(1, time - 1):
        if _check_winning_time(time, distance, x):
            # first winner!
            lowest = x - 1
            break

    highest = None
    # find highest that will still win
    for x in range(time - 1, 0, -1):
        if _check_winning_time(time, distance, x):
            highest = x
            break
    print(highest - lowest)
