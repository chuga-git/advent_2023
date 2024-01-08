import re


def find_symbols(text):
    symbols = re.findall(r"[^\d\s\.]", text)
    unique = ""

    for i in symbols:
        if i not in unique:
            unique += i

    return unique


def part_numbers(m, symbols):
    num_pos = {}
    sym_list = []
    part_list = {}
    total = 0
    sum_ratio = 0

    for row in range(len(m)):
        m[row] += "."
        buff_s = ""

        # buffer padding screws with the bounds - take len directly
        for col in range(len(m[row])):
            curr = m[row][col]

            if str.isdigit(curr):
                buff_s += curr
            else:
                if len(buff_s) >= 1:
                    num_pos[(row, col - len(buff_s))] = buff_s
                    buff_s = ""

                if curr in symbols:
                    sym_list += [(row, col)]

    for symb in sym_list:
        adj = []
        for num, num_val in num_pos.items():
            y1, x1 = num
            y2, x2 = symb
            length = len(num_val)

            # check for symbol in x - 1 and right x + len
            if (x1 - 1 <= x2 <= x1 + length) and (abs(y2 - y1) <= 1):
                part_list[num] = int(num_val)
                adj += [int(num_val)]
                total += int(num_val)

        if len(adj) == 2:
            sum_ratio += adj[0] * adj[1]

    return total, sum_ratio


if __name__ == "__main__":
    in_path = "day3.in"

    with open(in_path) as f_in:
        raw = f_in.read()
        lines = raw.splitlines()

    answer1, answer2 = part_numbers(lines, find_symbols(raw))
    print(f"Part 1: {answer1}\nPart 2: {answer2}")
