import re
from itertools import chain


def read_file_lines() -> list:
    with open("input.txt", "r") as f:
        return f.readlines()


def find_numbers_near_stars(previous_line: str, working_line: str, next_line: str) -> int:
    total = 0
    numbers_prev = re.finditer(r"\d+", previous_line)
    numbers_work = re.finditer(r"\d+", working_line)
    numbers_next = re.finditer(r"\d+", next_line)
    all_numbers = chain(numbers_prev, numbers_work, numbers_next)

    stars = re.finditer(r"\*", working_line)
    star_points = {}
    for star in stars:
        star_points[star.span()[0]] = []

    for number in all_numbers:
        span_number = number.span()
        start = span_number[0] if span_number[0] == 0 else span_number[0] - 1
        stop = span_number[1] if span_number[1] == len(working_line) else span_number[1] + 1
        for star_point in star_points:
            if star_point in range(start, stop):
                star_points[star_point].append(number.group())

    print(star_points)
    for _, numbers in star_points.items():
        if len(numbers) == 2:
            total += int(numbers[0]) * int(numbers[1])

    print(f"sum of line {total}")
    return total


def process_input(lines: list) -> int:
    total = 0

    for index, working_line in enumerate(lines):
        previous_line = "" if index == 0 else lines[index - 1]
        next_line = "" if index == len(lines) - 1 else lines[index + 1]
        total += find_numbers_near_stars(previous_line=previous_line.strip(),
                                         working_line=working_line.strip(),
                                         next_line=next_line.strip())

    return total


def main():
    lines = read_file_lines()
    print(f"Sum of gear ratio: {process_input(lines)}")


if __name__ == "__main__":
    main()
