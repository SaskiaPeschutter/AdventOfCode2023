def read_file_lines() -> list:
    with open("input.txt", "r") as f:
        return f.readlines()


# Part 1
colors_max = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_possible(color: str, amount: int) -> bool:
    return amount <= colors_max[color]


def process_if_game_possible(game: str) -> int:
    game_name, draws = game.strip().split(":")
    draws = draws.split(";")
    for picks in draws:
        pick = picks.split(",")
        for color in pick:
            colour_amount = color.split(" ")
            amount = int(colour_amount[1])
            color = colour_amount[2]
            if not is_possible(color=color, amount=amount):
                return 0
    game_number = game_name.split(" ")[1]
    return int(game_number)


def process_possible_game_counter(lines: list) -> int:
    return sum(process_if_game_possible(x) for x in lines)


# Part 2
def get_biggest(max: int, amount: int) -> int:
    return max if max > amount else amount


def process_game_power(game: str) -> int:
    minimum_color_amount = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    game_name, draws = game.strip().split(": ")
    draws = draws.split("; ")
    for picks in draws:
        pick = picks.split(", ")
        for color in pick:
            amount, color = color.split(" ")
            min_amount = int(minimum_color_amount[color])
            biggest = get_biggest(max=min_amount, amount=int(amount))
            minimum_color_amount[color] = biggest

    return minimum_color_amount["red"] * minimum_color_amount["green"] * minimum_color_amount["blue"]


def process_power_of_game_counter(lines: list) -> int:
    return sum(process_game_power(x) for x in lines)


def main():
    lines = read_file_lines()
    print(f"Sum of possible game ids : {process_possible_game_counter(lines)}")
    print(f"Power of min colors per game: {process_power_of_game_counter(lines)}")


if __name__ == "__main__":
    main()
