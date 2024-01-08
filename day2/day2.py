import re


def part_1(text):
    total = 0
    max_colors = {"blue": 14, "green": 13, "red": 12}

    for line in text:
        game_id = int(re.findall(r"Game (\d+):", line)[0])
        events = re.findall(r"(\d+ \w+)", line)
        possible = True

        for draw in events:
            num = int(draw.split()[0])
            color = draw.split()[1]

            if num > max_colors[color]:
                possible = False

        if possible:
            total += game_id

    return total


def part_2(text):
    total = 0
    for line in text:
        power = 1
        max_colors = {"blue": 0, "red": 0, "green": 0}
        game_id = int(re.findall(r"Game (\d+):", line)[0])
        events = re.findall(r"(\d+ \w+)", line)

        for draw in events:
            num = int(draw.split()[0])
            color = draw.split()[1]

            if num > max_colors[color]:
                max_colors[color] = num

        for i in max_colors:
            power *= max_colors[i]

        total += power

    return total


if __name__ == "__main__":
    in_path = "day2.in"

    with open(in_path) as f_in:
        lines = f_in.read().splitlines()

    part1_answer = part_1(lines)
    part2_answer = part_2(lines)
