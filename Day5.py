import re
import time


def read_file_lines() -> list:
    with open("input.txt", "r") as f:
        return f.readlines()


# Part 1
def get_seeds(lines: list) -> list:
    seed_numbers = lines[0].split(":")[1]
    return re.findall(r"\d+", seed_numbers)


def get_seed_pairs(lines: list) -> list:
    seed_pairs = []
    seed_numbers = lines[0].split(":")[1]
    seeds = re.findall(r"\d+", seed_numbers)
    for i in range(0, len(seeds) - 1, 2):
        seed_pairs.append({"start": int(seeds[i]), "range": int(seeds[i + 1])})
    return seed_pairs


def get_maps(lines: list):
    maps = []
    name = None
    ranges = []
    for line in lines[1:]:
        if ":" in line:
            if name:
                maps.append({name: ranges})
                ranges = []
            name = line.replace(":", "").strip()
        numbers = re.findall(r"\d+", line)
        if numbers:
            ranges.append({"destination": numbers[0], "source": numbers[1], "range": numbers[2]})
    maps.append({name: ranges})

    return maps


def find_mapping(seed: int, maps: dict):
    destination = seed
    for key, values in maps.items():
        for mapping in values:
            end_range = int(mapping["source"]) + int(mapping["range"])
            if seed in range(int(mapping["source"]), end_range):
                diff = seed - int(mapping["source"])
                destination = int(mapping["destination"]) + diff
                return destination
    return destination


def process_input_seed_list(lines: list) -> int:
    mappings = get_maps(lines)
    seeds = get_seeds(lines)
    destinations = []
    for seed in seeds:
        for maps in mappings:
            seed = find_mapping(int(seed), maps)
        destinations.append(seed)
    return min(destinations)


def process_input_seed_pairs(lines: list) -> int:
    skip_factor = 10000
    mappings = get_maps(lines)
    seeds_pairs = get_seed_pairs(lines)

    destinations = []
    old_destination = None
    for seeds in seeds_pairs:
        end = seeds["start"] + seeds["range"]
        for seed in range(seeds["start"], end, skip_factor):
            factor_destination = seed
            for maps in mappings:
                factor_destination = find_mapping(int(factor_destination), maps)
            new_destination = factor_destination
            if old_destination is not None:
                if old_destination + skip_factor != new_destination:
                    for between_destination in range(seed - skip_factor, seed, 1):
                        for maps in mappings:
                            between_destination = find_mapping(int(between_destination), maps)
                        destinations.append(between_destination)
                if seed + skip_factor > end:
                    for last_destination in range(seed, end, 1):
                        for maps in mappings:
                            last_destination = find_mapping(int(last_destination), maps)
                        destinations.append(last_destination)

            old_destination = factor_destination
            destinations.append(factor_destination)
    return min(destinations)


def main():
    lines = read_file_lines()
    print(f"Lowest Location number of seed list : {process_input_seed_list(lines)}")

    print(f"Lowest Location number of seed pairs : {process_input_seed_pairs(lines)}")


if __name__ == "__main__":
    main()
