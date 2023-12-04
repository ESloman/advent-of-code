"""Advent of Code 2023 Day 4."""

from advent_of_code.util import inputs


def _card_representation(line: str) -> tuple[int, dict[str]]:
    """Converts a line into a card representation.

    Args:
        line (str): the line to parse

    Returns:
        tuple[int, dict[str]]: the card number and card dict
    """
    name, numbers_line = line.split(":")
    *_, card_num = name.split(" ")
    winning, actual = _split_card(numbers_line)
    card = {"winning": winning, "actual": actual, "count": 1}
    return int(card_num), card


def _split_card(line: str) -> tuple[list[int], list[int]]:
    """Given a line, extracts the winning and actual card numbers.

    Args:
        line (str): the line to parse

    Returns:
        tuple[list[int], list[int]]: the winning and actual numbers
    """
    winning, actual = line.split("|")
    winning_numbers = [int(win) for win in winning.strip().split(" ") if win]
    actual_numbers = [int(act) for act in actual.strip().split(" ") if act]
    return winning_numbers, actual_numbers


def _get_score(winning_numbers: list[int], actual_numbers: list[int]) -> int:
    """Gets score from a scratchcard.

    For part one.

    Args:
        winning_numbers (list[int]): the winning numbers
        actual_numbers (list[int]): the actual numbers

    Returns:
        int: the score of a given card
    """
    score = 0
    for number in actual_numbers:
        if number in winning_numbers:
            if not score:
                score = 1
            else:
                score *= 2
    return score


def _get_winning_count(winning_numbers: list[int], actual_numbers: list[int]) -> int:
    """Gets winning number of numbers.

    For part two.

    Args:
        winning_numbers (list[int]): the winning numbers
        actual_numbers (list[int]): the actual numbers

    Returns:
        int: the number of winning actual numbers
    """
    score = 0
    for number in actual_numbers:
        if number in winning_numbers:
            score += 1
    return score


if __name__ == "__main__":
    lines = inputs.get_input()

    # part one
    total = 0
    for line in lines:
        ln = line.split(":")[-1]
        winning, actual = _split_card(ln)
        total += _get_score(winning, actual)
    print(total)

    # part two
    cards: dict[int, dict[str]] = {}
    for line in lines:
        num, card = _card_representation(line)
        cards[num] = card

    for card_num in cards:
        print(f"processing {card_num=}")
        count = cards[card_num]["count"]
        for _ in range(count):
            wins = _get_winning_count(cards[card_num]["winning"], cards[card_num]["actual"])
            for inc in range(wins):
                cards[card_num + inc + 1]["count"] += 1
    total_cards = sum([cards[key]["count"] for key in cards])
    print(total_cards)
