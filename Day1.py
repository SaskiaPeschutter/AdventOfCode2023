import re


def line_value(line):
    line = line.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace(
        "five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e")
    numbers = re.findall(r"\d", line)
    return int(numbers[0] + numbers[-1])


with open("input.txt") as f:
    lines = f.readlines()
    sum_all_lines = sum(line_value(x) for x in lines)

print(sum_all_lines)
