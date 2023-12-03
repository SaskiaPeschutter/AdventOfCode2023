import re


def read_file_lines() -> list:
    with open("input.txt", "r") as f:
        return f.readlines()


def is_symbol_near_number(text: str) -> bool:
    remaining = re.sub(r"\.", "", text)
    remaining = re.sub(r"\d+", "", remaining)
    if remaining:
        return True
    return False


def find_numbers_in_lines(previous_line: str, working_line: str, next_line: str) -> int:
    sum_line = 0

    numbers = re.finditer(r"\d+", working_line)
    for number in numbers:
        start, stop = number.span()
        start = start if start == 0 else start - 1
        stop = stop if stop == len(working_line) else stop + 1
        text = previous_line[start:stop] + working_line[start:stop] + next_line[start:stop]
        if is_symbol_near_number(text):
            sum_line += int(number.group())

    return sum_line


def process_input(lines: list) -> int:
    total = 0

    for index, working_line in enumerate(lines):
        previous_line = "" if index == 0 else lines[index - 1]
        next_line = "" if index == len(lines) - 1 else lines[index + 1]
        total += find_numbers_in_lines(previous_line=previous_line.strip(), working_line=working_line.strip(),
                                       next_line=next_line.strip())

    return total


def main():
    lines = read_file_lines()
    print(f"Sum of part ids : {process_input(lines)}")


if __name__ == "__main__":
    main()
