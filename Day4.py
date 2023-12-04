import re
from typing import Iterator


def line_iterator() -> Iterator[str]:
    for row in open("input.txt", "r"):
        yield row.strip()


def check_win_count(game_info: dict) -> int:
    value = 0
    for number in game_info["numbers"]:
        if number in game_info["winning_numbers"]:
            value += 1
            continue
    return value


def get_elements_in_line(line: str) -> dict:
    line = line.strip().split(":")[1].split(r"|")
    winning_numbers = re.findall(r"\d+", line[0])
    numbers = re.findall(r"\d+", line[1])

    return {"winning_numbers": winning_numbers, "numbers": numbers}


def process_input_count_wins() -> int:
    total = 0
    for scratch_card in line_iterator():
        game_info = get_elements_in_line(scratch_card)
        wins = check_win_count(game_info)
        win_count = 2 ** (wins - 1) if wins > 0 else 0
        total += win_count

    return total


def process_input_count_copies() -> int:
    total = 0
    copies = [1] * 11
    len_copies = len(copies)

    for scratch_card in line_iterator():
        game_info = get_elements_in_line(scratch_card)
        wins = check_win_count(game_info)
        card_amount = 1
        for i in range(len_copies):
            if i == 0:
                card_amount = copies[i]
                total += card_amount
            else:
                add = card_amount if wins > 0 else 0
                wins -= 1
                copies[i - 1] = copies[i] + add
    return total


def main():
    # Part 1
    sum_won_scratch_cards = process_input_count_wins()
    print(f"Sum of Scratch Card Wins: {sum_won_scratch_cards}")

    # Part 2
    sum_scratch_cards = process_input_count_copies()
    print(f"Sum Scratch Cards: {sum_scratch_cards}")


if __name__ == "__main__":
    main()
