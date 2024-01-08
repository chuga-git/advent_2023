import re


def part_1(list_in):
    total = 0

    for line in list_in:
        digits = re.findall(r"\d", line)
        total += int(digits[0] + digits[-1])

    return total


def part_2(list_in):
    table = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    total = 0

    for line in list_in:
        digits = re.findall(
            r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line
        )
        for i in range(len(digits)):
            if digits[i] in table:
                digits[i] = table[digits[i]]

        total += int(digits[0] + digits[-1])

    return total


if __name__ == "__main__":
    in_path = "day1.in"

    with open(in_path) as f:
        lines = f.read().splitlines()

    print("Part 1 answer:", part_1(lines))
    print("Part 2 answer:", part_2(lines))
