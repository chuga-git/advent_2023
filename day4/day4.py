from collections import defaultdict


def part_1(text) -> dict:
    cards = defaultdict(list)
    total = 0
    for line in text:
        card_num = int(line[5 : line.find(":")])
        winning_nums = line[line.find(":") + 1 : line.find("|")].strip().split()
        owned_nums = line[line.find("|") + 1 :].strip().split()
        matching = []
        for i in owned_nums:
            if i in winning_nums:
                matching += [i]
                cards[card_num] += [i]

        if len(matching) != 0:
            total += 2 ** (len(matching) - 1)

    return total


def parse_line(line):
    winning_nums = line[line.find(":") + 1 : line.find("|")].strip().split()
    owned_nums = line[line.find("|") + 1 :].strip().split()
    matches = 0

    for i in owned_nums:
        if i in winning_nums:
            matches += 1

    return matches


def part_2(text):
    cards = [1] * len(text)
    for idx, line in enumerate(text):
        matches = parse_line(line)

        for n in range(matches):
            cards[idx + n + 1] += cards[idx]

    return sum(cards)


if __name__ == "__main__":
    in_path = "day4.in"

    with open(in_path) as f_in:
        lines = f_in.read().splitlines()

    print("Part 1 answer:", part_1(lines))
    print("Part 2 answer:", part_2(lines))
