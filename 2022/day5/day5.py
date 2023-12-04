import copy

from advent_of_code.util import inputs


def _get_crates_from_row(line: str, crates: dict[int, list[str]]) -> None:
    """Extracts the crates from a row.

    Args:
        line (str): the line to process
        crates (dict[int, list[str]]): the crates representation to fill
    """
    length = len(line)
    x = 0
    column = 1
    while x < length:
        crate = line[x : x + 3].strip(" ").strip("[").strip("]")
        if column not in crates:
            crates[column] = []
        if crate:
            crates[column].insert(0, crate)
        x += 4
        column += 1


def _process_single_move(move: str, crates: dict[int, list[str]]) -> None:
    """Moves the crates one at a time.

    As per part one.

    Args:
        move (str): the move string
        crates (dict[int, list[str]]): the crates representation
    """
    count, source, destination = (int(part) for part in move.split(" ") if part.isnumeric())

    for _ in range(count):
        val = crates[source].pop(-1)
        crates[destination].append(val)


def _process_multi_move(move: str, crates: dict[int, list[str]]) -> None:
    """Moves the crates a few at a time.

    As per part two.

    Args:
        move (str): the move string
        crates (dict[int, list[str]]): the crates representation
    """
    count, source, destination = (int(part) for part in move.split(" ") if part.isnumeric())
    vals = []
    for _ in range(count):
        val = crates[source].pop(-1)
        vals.insert(0, val)

    crates[destination].extend(vals)


if __name__ == "__main__":
    lines = inputs.get_input()

    crates: dict[int, list[str]] = {}
    for line in lines:
        if "[" not in line:
            # end of crates
            break
        _get_crates_from_row(line, crates)

    first_move_index = lines.index(next(line for line in lines if "move " in line))

    moves = lines[first_move_index:]

    part_one_crates = copy.deepcopy(crates)
    part_two_crates = copy.deepcopy(crates)

    # part one
    for move in moves:
        _process_single_move(move, part_one_crates)

    message = ""
    for key in part_one_crates:
        message += part_one_crates[key][-1]
    print(message)

    # part two
    for move in moves:
        _process_multi_move(move, part_two_crates)

    message = ""
    for key in part_two_crates:
        message += part_two_crates[key][-1]
    print(message)
