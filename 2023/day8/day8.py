"""Advent of Code 2023 Day 8."""

import math

from advent_of_code.util import inputs


def _map_node(line: str) -> tuple[str, tuple[str, str]]:
    """Gets the node and two pathing nodes from the line.

    Args:
        line (str): the line to process

    Returns:
        tuple[str, tuple[str, str]]: the parent node, and the two child nodes
    """
    key, nodes = line.split(" = ")
    nodes: tuple[str, str] = tuple(n.strip("(").strip(")") for n in nodes.split(", "))
    return key, nodes


def _map_nodes(lines: list[str]) -> dict[str, tuple[str, str]]:
    """Gets the full node map.

    Args:
        lines (list[str]): input lines

    Returns:
        dict[str, tuple[str, str]]: the node map
    """
    node_map = {}
    for line in lines:
        key, nodes = _map_node(line)
        node_map[key] = nodes
    return node_map


if __name__ == "__main__":
    lines = inputs.get_input()

    directions: str = lines[0]
    node_map = _map_nodes(lines[2:])

    # part one
    start = "AAA"
    current_node = start
    count = 0
    while True:
        for direction in directions:
            count += 1
            idx = 0 if direction == "L" else 1
            current_node = node_map[current_node][idx]
            if current_node == "ZZZ":
                break
        else:
            continue
        break
    print(count)

    # part two
    starting_nodes = [node for node in node_map if node[-1] == "A"]
    node_counts = {node: 0 for node in starting_nodes}
    for start_node in starting_nodes:
        count = 0
        current_node = start_node
        while True:
            for direction in directions:
                count += 1
                idx = 0 if direction == "L" else 1
                current_node = node_map[current_node][idx]

                if current_node[-1] == "Z":
                    break
            else:
                continue
            break
        node_counts[start_node] = count
    print(math.lcm(*node_counts.values()))
