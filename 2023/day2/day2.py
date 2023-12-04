"""Advent of Code 2023 Day 2."""

from advent_of_code.util import inputs

_MIN_RED = 12
_MIN_GREEN = 13
_MIN_BLUE = 14


def _process_round_part_one(rnd: str) -> bool:
    """Processes a given round for part one.

    Checks to see if it would have been possible for the bag to contain
    no more than 12 red, 13 green, and 14 blue cubes.

    Input in the format:
        3 blue, 4 red
        1 red, 2 green
        3 green, 15 blue, 14 red

    Args:
        rnd (str): the round in the above format

    Returns:
        bool: whether it would have been possible or not
    """
    cubes_txt = rnd.strip().split(", ")
    for cube_type in cubes_txt:
        num, colour = cube_type.split(" ")
        match colour:
            case "red":
                if int(num) > _MIN_RED:
                    return False
            case "green":
                if int(num) > _MIN_GREEN:
                    return False
            case "blue":
                if int(num) > _MIN_BLUE:
                    return False
    return True


def _process_round_part_two(rnd: str) -> tuple[int, int, int]:
    """Processes a given round for part two.

    Counts the number of red, green, and blue cubes for each round.

    Input in the format:
        3 blue, 4 red
        1 red, 2 green
        3 green, 15 blue, 14 red

    Args:
        rnd (str): the round in the above format

    Returns:
        tuple[int, int, int]: the number of red, green, and blue cubes
    """
    cubes_txt = rnd.strip().split(", ")
    red, green, blue = 0, 0, 0
    for cube_type in cubes_txt:
        num, colour = cube_type.split(" ")
        match colour:
            case "red":
                red = int(num)
            case "green":
                green = int(num)
            case "blue":
                blue = int(num)
    return red, green, blue


def _process_line_part_one(line: str) -> int:
    """Processes a given line for part one.

    Checks if all the rounds in a game are possible to play with
    12 red, 13 green, and 14 blue cubes. Returns 0 if not possible or the
    game number if it is possible.

    Args:
        line (str): the line to process

    Returns:
        int: the game number if possible, or 0
    """
    game_txt, games_txt = line.split(":")
    game_num = int(game_txt.split(" ")[1])

    rounds = games_txt.split("; ")
    for rnd in rounds:
        possible = _process_round_part_one(rnd)
        if not possible:
            return 0
    return game_num


def _process_line_part_two(line: str) -> int:
    """Processes a given line for part two.

    Finds the minimum number of red, green, and blue cubes needed
    for a given game. Multiples these together to produce the power of a game.

    Args:
        line (str): the line to process

    Returns:
        int: the game's power
    """
    game_txt, games_txt = line.split(":")
    int(game_txt.split(" ")[1])

    rounds = games_txt.split("; ")
    min_red, min_green, min_blue = 0, 0, 0
    for rnd in rounds:
        red, green, blue = _process_round_part_two(rnd)
        min_red = max(min_red, red)
        min_green = max(min_green, green)
        min_blue = max(min_blue, blue)

    return min_red * min_green * min_blue


if __name__ == "__main__":
    lines = inputs.get_input()

    # part one
    games = []
    for line in lines:
        num = _process_line_part_one(line)
        games.append(num)
    print(f"Sum of valid games is: {sum(games)}")

    # part two
    powers = []
    for line in lines:
        num = _process_line_part_two(line)
        powers.append(num)
    print(f"Powers of all games is: {sum(powers)}.")
