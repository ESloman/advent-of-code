"""Advent of Code 2023 Day 7."""

from enum import IntEnum

from advent_of_code.util import inputs

CARD_ORDER = "23456789TJQKA"


class HandType(IntEnum):
    """Class to represent the hand types."""

    FIVE_OF_A_KIND = 0
    FOUR_OF_A_KIND = 1
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7
    NONE = 8


class Hand:
    """Represents a hand with it's given bid."""

    def __init__(self, hand: str, bid: int, part_two: bool = False) -> None:
        """Initialisation method.

        Args:
            hand (str): the 5 card hand
            bid (int): the bid associated with the hand
            part_two (bool, optional): whether to reclassify or not. Defaults to False.
        """
        self.hand: str = hand
        self.bid: int = bid
        self.part_two = part_two
        self.hand_type: HandType = self._classify_hand()

        if self.part_two and "J" in self.hand and self.hand_type != HandType.FIVE_OF_A_KIND:
            # only want to reclassify if we're part two and have Js in our hand
            self.hand_type = self._reclassify_hand()

    def __repr__(self) -> str:
        """Make sure we can pretty print the class."""
        return f"{self.hand}: {HandType(self.hand_type).name}"

    def __lt__(self, other: "Hand") -> bool:
        """Enable comparison between Hands.

        If the hand types are different, just return if we're less than the other.
        Otherwise, go through the card order and compare each card.

        Args:
            other (Hand): the item being compared against
        """
        if self.hand_type == other.hand_type:
            for idx in range(len(self.hand)):
                if self.hand[idx] == other.hand[idx]:
                    # move on to next card
                    continue
                return CARD_ORDER.index(self.hand[idx]) > CARD_ORDER.index(other.hand[idx])

        return self.hand_type < other.hand_type

    def _classify_hand(self) -> HandType:  # noqa: PLR0911
        """Classify hand.

        Based on the cards in the hand, return the matching HandType.

        Returns:
            HandType: the hand's HandType
        """
        for card in sorted(self.hand):
            match self.hand.count(card):
                case 5:
                    return HandType.FIVE_OF_A_KIND
                case 4:
                    return HandType.FOUR_OF_A_KIND
                case 3:
                    # check the other card types
                    other_cards = [_card for _card in self.hand if _card != card]
                    if other_cards[0] == other_cards[1]:
                        return HandType.FULL_HOUSE
                    return HandType.THREE_OF_A_KIND
                case 2:
                    # check other card types
                    other_cards = [_card for _card in self.hand if _card != card]
                    if len(set(other_cards)) == 2:  # noqa: PLR2004
                        # two other cards - meaning we have at least two pairs
                        return HandType.TWO_PAIR
                    if len(set(other_cards)) == 3:  # noqa: PLR2004
                        # each of the other cards is different
                        return HandType.ONE_PAIR
                case 1:
                    if len(set(self.hand)) == 5:  # noqa: PLR2004
                        # 5 unique cards
                        return HandType.HIGH_CARD
        return HandType.HIGH_CARD

    def _reclassify_hand(self) -> HandType:  # noqa: PLR0911
        """Reclassify hand.

        Used in part two only. If we contain jokers, then we can upgrade our hand.
        Look at our current hand type and work out which hand type we can upgrade to.

        Returns:
            HandType: the re-calculated HandType (might be the same)
        """
        # we know that we're not FIVE of a KIND
        # and that we have at least one J
        match self.hand.count("J"):
            # match base on number of jokers
            case 1:
                # only got one joker
                match self.hand_type:
                    case HandType.FOUR_OF_A_KIND:
                        return HandType.FIVE_OF_A_KIND
                    case HandType.THREE_OF_A_KIND:
                        return HandType.FOUR_OF_A_KIND
                    case HandType.TWO_PAIR:
                        return HandType.FULL_HOUSE
                    case HandType.ONE_PAIR:
                        return HandType.THREE_OF_A_KIND
                    case HandType.HIGH_CARD:
                        return HandType.ONE_PAIR
            case 2:
                match self.hand_type:
                    case HandType.THREE_OF_A_KIND | HandType.FULL_HOUSE:
                        return HandType.FIVE_OF_A_KIND
                    case HandType.TWO_PAIR:
                        return HandType.FOUR_OF_A_KIND
                    case HandType.ONE_PAIR:
                        return HandType.THREE_OF_A_KIND
            case 3:
                match self.hand_type:
                    case HandType.THREE_OF_A_KIND:
                        return HandType.FOUR_OF_A_KIND
                    case HandType.FULL_HOUSE:
                        return HandType.FIVE_OF_A_KIND
            case 4:
                return HandType.FIVE_OF_A_KIND
        return self.hand_type


def _split_hands_and_bids(line: str, part_two: bool = False) -> Hand:
    hand, bid = line.split(" ")
    return Hand(hand, int(bid), part_two)


if __name__ == "__main__":
    lines = inputs.get_input()

    # part one
    hands: list[Hand] = [_split_hands_and_bids(line) for line in lines]
    hands = sorted(hands, reverse=True)
    winnings = []
    for idx in range(len(hands)):
        hand = hands[idx]
        rank = idx + 1
        winning = rank * hand.bid
        winnings.append(winning)
    print(sum(winnings))

    # part two
    # re-organise card order to move J to the front
    CARD_ORDER.replace("J", "")
    CARD_ORDER = "J" + CARD_ORDER

    hands: list[Hand] = [_split_hands_and_bids(line, True) for line in lines]
    hands = sorted(hands, reverse=True)
    winnings = []
    for idx in range(len(hands)):
        hand = hands[idx]
        rank = idx + 1
        winning = rank * hand.bid
        winnings.append(winning)
    print(sum(winnings))
