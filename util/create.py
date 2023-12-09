"""Script for creating basic day structure."""

import argparse
import os
from pathlib import Path

MIN_YEAR = 2015
MAX_YEAR = 2030
MIN_DAY = 0
MAX_DAY = 25

PY_FILE_LINES = [
    "\n\nfrom advent_of_code.util import inputs",
    "\n\n\n",
    'if __name__ == "__main__":\n',
    "    lines = inputs.get_example_input()\n",
]


def _create_day_structure(year: int, day: int) -> None:
    """Creates the directories and empty files.

    Will create the "advent_of_code/YEAR/DAY/" directory and then create:
    - empty example_input.txt
    - empty input.txt
    = dayDAY.py with the standard boilerplate

    Args:
        year (int): the year
        day (int): the day
    """
    path = Path(__file__)
    root = path.parent.parent
    day_path = root.joinpath(str(year), f"day{day}")

    os.makedirs(day_path, exist_ok=True)
    print(f"Created dirs: {day_path}")

    example_input_path = day_path.joinpath("example_input.txt")
    if not example_input_path.exists():
        with open(example_input_path, "w+", encoding="utf-8"):
            print("Created example_input.txt")

    input_path = day_path.joinpath("input.txt")
    if not input_path.exists():
        with open(input_path, "w+", encoding="utf-8"):
            print("Created input.txt")

    py_path = day_path.joinpath(f"day{day}.py")
    if not py_path.exists():
        with open(py_path, "w+", encoding="utf-8") as pyfile:
            pyfile.write(f'"""Advent of Code {year} Day {day}."""')
            pyfile.writelines(PY_FILE_LINES)
            print("Created py file.")

    print("Created files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Creates the boilerplate for a new day. Requires a year and a day number."
    )

    _, args = parser.parse_known_args()

    if len(args) != 2:  # noqa: PLR2004
        parser.error("Please provide exactly one year and one day.")

    year = int(args[0])
    day = int(args[1])

    if not (MIN_YEAR <= year < MAX_YEAR):
        parser.error(f"{year} - not a valid year.")

    if not (MIN_DAY < day <= MAX_DAY):
        parser.error(f"{day} - not a valid day.")

    _create_day_structure(year, day)
