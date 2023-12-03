"""Advent of Code 2023 Day 3."""

ADJACENT_GEAR_NUMBERS = 2


class Num:
    """Represents a number in our grid.

    Each number is at least one digit long. Each digit has a separte co-ordinate
    in our grid.
    """

    def __init__(self, value: int, coords: list[tuple[int, int]]) -> "Num":
        """Initialiser."""
        self.coords = coords
        self.value = value

    def __repr__(self) -> str:
        """Nicer printing."""
        return f"{self.value}: {self.coords}"


def _make_grid(lines: list[str]) -> list[list[str]]:
    """Turns out list of lines into a grid.

    Args:
        lines (list[str]): a list of lines to process

    Returns:
        list[list[str]]: our grid
    """
    grid: list[list[str]] = []
    for x in range(len(lines)):
        grid.append([])
        line = lines[x]
        for y in line:
            grid[x].append(y)
    return grid


def _find_numbers(grid: list[list[str]]) -> list[Num]:
    """Finds all the numbers in the grid.

    Args:
        grid (list[list[str]]): the grid to process

    Returns:
        list[Num]: the list of Nums representing the numbers
    """
    numbers: list[Num] = []
    for x in range(len(grid)):
        coords = []
        number = False
        value = ""
        row = grid[x]
        for y in range(len(row)):
            item = grid[x][y]
            if item.isnumeric():
                coords.append((x, y))
                value += item
                number = True
            else:
                if number:
                    num = Num(int(value), coords)
                    numbers.append(num)
                number = False
                value = ""
                coords = []
        if number:
            num = Num(int(value), coords)
            numbers.append(num)
    return numbers


def _find_symbols(grid: list[list[str]]) -> dict[tuple, str]:
    """Finds all the symbols in the grid.

    Returns the symbols as a dictionary with the co-ordinates as keys (unique) and the given
    symbol as the values.

    Args:
        grid (list[list[str]]): the grid to find symbols in.

    Returns:
        dict[tuple, str]: the found symbols
    """
    symbols: dict[tuple, str] = {}
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] != "." and not grid[x][y].isnumeric():
                # y is a symbol
                symbols[(x, y)] = grid[x][y]
    return symbols


def _find_adjacent_numbers(symbol_coords: tuple[int, int], numbers: list[Num], grid: list[list[str]]) -> list[Num]:
    """Given a symbol co-ordinate, find the adjacent numbers.

    Args:
        symbol_coords (tuple[int, int]): the coord of the symbol
        numbers (list[Num]): the list of numbers
        grid (list[list[str]]): the grid

    Returns:
        list[Num]: the list of adjacent numbers
    """
    adjacency = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    adjacent_numbers = []
    for vector in adjacency:
        x = symbol_coords[0] + vector[0]
        y = symbol_coords[1] + vector[1]

        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid):
            # skip out of bounds
            continue

        item: str = grid[x][y]
        if not item.isnumeric():
            continue

        # else find the corresponding number
        num = next(number for number in numbers if (x, y) in number.coords)
        if num not in adjacent_numbers:
            adjacent_numbers.append(num)
    return adjacent_numbers


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as file:
        lines = [line.strip("\n") for line in file.readlines()]

    grid = _make_grid(lines)
    numbers = _find_numbers(lines)
    symbols = _find_symbols(grid)

    # part one
    valid_numbers: list[Num] = []
    for symbol_coord in symbols:
        adjacent_nums = _find_adjacent_numbers(symbol_coord, numbers, grid)
        for num in adjacent_nums:
            if num not in valid_numbers:
                valid_numbers.append(num)

    print(sum([v.value for v in valid_numbers]))

    # part two
    gear_ratios: list[int] = []
    for symbol_coord in symbols:
        if symbols[symbol_coord] != "*":
            # not a gear
            continue
        adjacent_nums = _find_adjacent_numbers(symbol_coord, numbers, grid)
        if len(adjacent_nums) != ADJACENT_GEAR_NUMBERS:
            # not a gear
            continue
        gear_ratios.append(adjacent_nums[0].value * adjacent_nums[1].value)

    print(sum(gear_ratios))
