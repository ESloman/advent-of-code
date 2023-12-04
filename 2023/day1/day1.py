"""Advent of Code 2023 Day 1."""

from advent_of_code.util import inputs


def _process_line_part_one(line: str) -> int:
    """Calculates the value of the line.

    According to part 1 of day 1.

    Args:
        line (str): the inputted line

    Returns:
        int: the total sum for this line
    """
    nums = []
    for index in line:
        try:
            num = int(index)
            nums.append(num)
        except ValueError:
            continue
    first = nums[0]
    last = nums[-1]
    return int(f"{first}{last}")


def _process_line_part_two(line: str) -> int:  # noqa: PLR0912,C901
    """Calculates the value of the line.

    According to part 2 of day 1.

    Args:
        line (str): the inputted line

    Returns:
        int: the total sum for this line
    """
    nums = []
    for index in range(len(line)):
        try:
            num = int(line[index])
            nums.append(num)
        except ValueError:
            # not a number - do second part
            match line[index]:
                case "o":
                    if line[index + 1 : index + 3] == "ne":
                        nums.append(1)
                case "t":
                    if line[index + 1 : index + 3] == "wo":
                        nums.append(2)
                    elif line[index + 1 : index + 5] == "hree":
                        nums.append(3)
                case "f":
                    if line[index + 1 : index + 4] == "our":
                        nums.append(4)
                    elif line[index + 1 : index + 4] == "ive":
                        nums.append(5)
                case "s":
                    if line[index + 1 : index + 3] == "ix":
                        nums.append(6)
                    elif line[index + 1 : index + 5] == "even":
                        nums.append(7)
                case "e":
                    if line[index + 1 : index + 5] == "ight":
                        nums.append(8)
                case "n":
                    if line[index + 1 : index + 4] == "ine":
                        nums.append(9)
                case _:
                    continue
    first = nums[0]
    last = nums[-1]
    return int(f"{first}{last}")


if __name__ == "__main__":
    lines = inputs.get_input()

    numbers = []
    for line in lines:
        num = _process_line_part_one(line)
        numbers.append(num)
    print(f"Part One total was: {sum(numbers)}")

    numbers = []
    for line in lines:
        num = _process_line_part_two(line)
        numbers.append(num)
    print(f"Part two total was: {sum(numbers)}")
