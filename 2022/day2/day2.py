"""Advent of code 2022 Day 2."""

from enum import IntEnum

from advent_of_code.util import inputs


class Results(IntEnum):
    """Enum for results score values."""

    WIN = 6
    LOSE = 0
    DRAW = 3


class Shapes(IntEnum):
    """Enum for shapes score values."""

    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def _calculate_score_part_one(line: str) -> int:
    """Calculates the score in accordance with part one.

    Args:
        line (str): the line to calculate the score for

    Returns:
        int: the score for this line
    """
    opp, shape = line.split(" ")

    score = 0
    match shape:
        case "X":
            score += Shapes.ROCK
        case "Y":
            score += Shapes.PAPER
        case "Z":
            score += Shapes.SCISSORS

    match opp:
        case "A":
            # opponent played rock
            match shape:
                case "X":
                    # draw
                    score += Results.DRAW
                case "Y":
                    # lose
                    score += Results.WIN
                case "Z":
                    # lose
                    score += Results.LOSE
        case "B":
            # opponent played paper
            match shape:
                case "X":
                    # lose
                    score += Results.LOSE
                case "Y":
                    # draw
                    score += Results.DRAW
                case "Z":
                    # win
                    score += Results.WIN
        case "C":
            # opponent played scissors
            match shape:
                case "X":
                    # lose
                    score += Results.WIN
                case "Y":
                    # draw
                    score += Results.LOSE
                case "Z":
                    # win
                    score += Results.DRAW
    return score


def _calculate_score_part_two(line: str) -> int:
    """Calculates the score in accordance with part two.

    Args:
        line (str): the line to calculate the score for

    Returns:
        int: the score for this line
    """
    opp, shape = line.split(" ")

    score = 0

    match opp:
        case "A":
            # opponent played rock
            match shape:
                case "X":
                    # lose
                    score += Results.LOSE
                    score += Shapes.SCISSORS
                case "Y":
                    # draw
                    score += Results.DRAW
                    score += Shapes.ROCK
                case "Z":
                    # win
                    score += Results.WIN
                    score += Shapes.PAPER
        case "B":
            # opponent played paper
            match shape:
                case "X":
                    # lose
                    score += Results.LOSE
                    score += Shapes.ROCK
                case "Y":
                    # draw
                    score += Results.DRAW
                    score += Shapes.PAPER
                case "Z":
                    # win
                    score += Results.WIN
                    score += Shapes.SCISSORS
        case "C":
            # opponent played scissors
            match shape:
                case "X":
                    # lose
                    score += Results.LOSE
                    score += Shapes.PAPER
                case "Y":
                    # draw
                    score += Results.DRAW
                    score += Shapes.SCISSORS
                case "Z":
                    # win
                    score += Results.WIN
                    score += Shapes.ROCK
    return score


if __name__ == "__main__":
    lines = inputs.get_input()

    total_score_part_one, total_score_part_two = 0, 0
    for line in lines:
        part_one = _calculate_score_part_one(line)
        part_two = _calculate_score_part_two(line)
        total_score_part_one += part_one
        total_score_part_two += part_two

    print(total_score_part_one)
    print(total_score_part_two)
