"""Input utility for Advent of Code stuff."""

import inspect
import os
from pathlib import Path


def _get_lines(filename: str | Path) -> list[str]:
    """Gets the lines from a file."""
    with open(filename, encoding="utf-8") as file:
        return [line.strip("\n") for line in file.readlines()]


def _get_aoc_day_path(filename: str) -> Path:
    """Gets the full AOC path of the file.

    Assuming we're not calling the specific script from within the YEAR/DAY directory so the relative path to
    the specified input file is likely wrong. Work out which file called this one and build an absolute path
    to the input file. Return that Path.

    Args:
        filename (str): the filename to make absolute

    Returns:
        Path: the absolute Path
    """
    return Path(os.path.dirname(inspect.getmodule(inspect.stack()[2][0]).__file__), filename)


def get_example_input_part_two() -> list[str]:
    """Gets the lines from the 'example_input' file."""
    return _get_lines(_get_aoc_day_path("example_input_pt2.txt"))


def get_example_input() -> list[str]:
    """Gets the lines from the 'example_input' file."""
    return _get_lines(_get_aoc_day_path("example_input.txt"))


def get_input() -> list[str]:
    """Gets the lines from the 'input.txt' file."""
    return _get_lines(_get_aoc_day_path("input.txt"))
