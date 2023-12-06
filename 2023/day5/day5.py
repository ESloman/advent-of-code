"""Advent of Code 23 Day 5."""

from itertools import batched

from advent_of_code.util import inputs


def _extract_seeds(line: str) -> list[int]:
    """Extracts seeds from the line.

    Args:
        line (str): the line to extract the seeds from

    Returns:
        list[int]: the list of seeds
    """
    return [int(seed) for seed in line.replace("seeds: ", "").split(" ")]


def _map_numbers(destination_start: int, source_start: int, length: int) -> tuple[range, range]:
    """_summary_.

    Args:
        source_start (int): _description_
        destination_start (int): _description_
        length (int): _description_
        _map (dict[int, int]): _description_

    Returns:
        dict: _description_
    """
    source_range = range(source_start, source_start + length)
    destination_range = range(destination_start, destination_start + length)
    return source_range, destination_range


def _get_dst_from_map(num: int, _map: dict[range, range]) -> int | None:
    for key in _map:
        if num in key:
            idx = key.index(num)
            return _map[key][idx]
    return None


def _get_seed_location(seed: int, maps: dict[str, dict[range, range]]) -> int:
    soil_num = _get_dst_from_map(seed, maps["seed-to-soil"])
    soil_num = soil_num if soil_num is not None else seed
    fert_num = _get_dst_from_map(soil_num, maps["soil-to-fertilizer"])
    fert_num = fert_num if fert_num is not None else soil_num
    water_num = _get_dst_from_map(fert_num, maps["fertilizer-to-water"])
    water_num = water_num if water_num is not None else fert_num
    light_num = _get_dst_from_map(water_num, maps["water-to-light"])
    light_num = light_num if light_num is not None else water_num
    temp_num = _get_dst_from_map(light_num, maps["light-to-temperature"])
    temp_num = temp_num if temp_num is not None else light_num
    hum_num = _get_dst_from_map(temp_num, maps["temperature-to-humidity"])
    hum_num = hum_num if hum_num is not None else temp_num
    location_num = _get_dst_from_map(hum_num, maps["humidity-to-location"])
    return location_num if location_num is not None else hum_num


if __name__ == "__main__":
    lines = inputs.get_input()

    seeds = _extract_seeds(lines[0])
    print(seeds)

    maps: dict[str, dict[int, int]] = {}
    current_map = None
    for line in lines[1:]:
        if not line:
            continue

        if "map" in line:
            # new map!
            map_name = line.split(" ")[0]
            print(f"Calculating map for {map_name}")
            if map_name not in maps:
                maps[map_name] = {}
            current_map = maps[map_name]
            continue

        src_rng, dst_rng = _map_numbers(*[int(ln) for ln in line.split(" ")])
        current_map[src_rng] = dst_rng

    # part one
    locations_part_one = [_get_seed_location(seed, maps) for seed in seeds]
    print(min(locations_part_one))

    # very inefficient
    # won't actually finish but run out of memory and die
    # should _theoretically_ find a solution if unlimited memory and processing power
    # need to work out how to optimise it to finish it
    # # part two
    locations_part_two = []
    for pair in batched(seeds, 2):
        locations_part_two.extend(_get_seed_location(seed, maps) for seed in range(pair[0], sum(pair)))
    print(min(locations_part_two))
