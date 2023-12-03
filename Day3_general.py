import re
from typing import Iterator, Callable


def line_iterator() -> Iterator[str]:
    for row in open("input.txt", "r"):
        yield row.strip()


def check_gear_condition(main_element: dict, conditions: list) -> int:
    numbers_in_range = []
    for condition in conditions:
        start = condition["start"] - 1 if condition["start"] > 0 else condition["start"]
        stop = condition["stop"] + 1
        if main_element["start"] in range(start, stop):
            numbers_in_range.append(condition["match"])
    if len(numbers_in_range) == 2:
        return int(numbers_in_range[0]) * int(numbers_in_range[1])
    return 0


def check_part_id(main_element: dict, conditions: list) -> int:
    start = main_element["start"] - 1 if main_element["start"] > 0 else main_element["start"]
    stop = main_element["stop"] + 1
    for condition in conditions:
        print(condition)
        if condition["start"] in range(start, stop):
            return int(main_element["match"])
    return 0


def check_conditions(previous_line_info: dict, working_line_info: dict, next_line_info: dict,
                     condition_function: Callable) -> int:
    sum_line = 0
    conditions = previous_line_info["conditions"] + working_line_info["conditions"] + next_line_info["conditions"]
    for main_element in working_line_info["main"]:
        sum_line += int(condition_function(main_element, conditions))

    return sum_line


def get_elements_in_line(line: str, search: str) -> list:
    elements = re.finditer(search, line.strip())
    elements_info = []
    for element in elements:
        span_number = element.span()
        elements_info.append({"match": element.group(),
                              "start": span_number[0],
                              "stop": span_number[1]})

    return elements_info


def process_input(main_search_string: str, condition_search_string: str, condition_function: Callable) -> int:
    total = 0

    next_line_info = {"main": [], "conditions": []}
    working_line_info = {"main": [], "conditions": []}

    for index, working_line in enumerate(line_iterator()):
        previous_line_info = working_line_info
        working_line_info = next_line_info

        next_line_info = {"main": get_elements_in_line(working_line, main_search_string),
                          "conditions": get_elements_in_line(working_line, condition_search_string)}

        total += check_conditions(previous_line_info=previous_line_info,
                                  working_line_info=working_line_info,
                                  next_line_info=next_line_info,
                                  condition_function=condition_function)

    # process last line
    previous_line_info = working_line_info
    working_line_info = next_line_info

    next_line_info = {"main": [], "conditions": []}

    total += check_conditions(previous_line_info=previous_line_info,
                              working_line_info=working_line_info,
                              next_line_info=next_line_info,
                              condition_function=condition_function)
    return total


def main():
    # Part 1
    number_search = r"\d+"
    condition_search = r"[^.\d]+"
    sum_part_ids = process_input(main_search_string=number_search,
                                 condition_search_string=condition_search,
                                 condition_function=check_part_id)
    print(f"Sum of part ids : {sum_part_ids}")

    # Part 2
    star_search = r"\*"
    condition_search = r"\d+"
    sum_gear_ratio = process_input(main_search_string=star_search,
                                   condition_search_string=condition_search,
                                   condition_function=check_gear_condition)
    print(f"Sum of gear ratio: {sum_gear_ratio}")  #


if __name__ == "__main__":
    main()
