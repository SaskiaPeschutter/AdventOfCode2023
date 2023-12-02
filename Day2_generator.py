from functools import reduce
from typing import Iterator, Callable


def game_iterator() -> Iterator[str]:
    for row in open("input.txt", "r"):
        yield row.strip()


def get_color_picks(game: str) -> (str, int):
    draws = game.split(": ")[1].split("; ")
    for color_picks in draws:
        color_pick = color_picks.split(", ")
        for color in color_pick:
            amount, color = color.split(" ")
            yield color, amount


# Part 1
colors_max = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_possible(color: str, amount: int) -> bool:
    return amount <= colors_max[color]


def get_game_id(game: str) -> int:
    return int(game.split(": ")[0].split(" ")[1])


def get_id_if_game_is_possible(game: str) -> int:
    for color, amount in get_color_picks(game):
        if not is_possible(color=color, amount=int(amount)):
            return 0
    return get_game_id(game)


# Part 2
def power_of_list_elements(power_list: list) -> int:
    power_result = reduce(lambda a, b: a * b, power_list, 1)
    return power_result


def get_biggest(previous_max: int, amount: int) -> int:
    return previous_max if previous_max > amount else amount


def get_power_of_min_color_amounts(game: str) -> int:
    minimum_color_amount = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for color, amount in get_color_picks(game):
        min_amount = int(minimum_color_amount[color])
        biggest = get_biggest(previous_max=min_amount, amount=int(amount))
        minimum_color_amount[color] = biggest
    return power_of_list_elements(list(minimum_color_amount.values()))


def process_game(function: Callable) -> int:
    return sum(function(game) for game in game_iterator())


def main():
    print(f"Sum of possible game ids : {process_game(get_id_if_game_is_possible)}")
    print(f"Power of min colors per game: {process_game(get_power_of_min_color_amounts)}")


if __name__ == "__main__":
    main()
