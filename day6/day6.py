from rich import print

in_path = "day6.in"

with open(in_path) as f_in:
    lines = f_in.read().splitlines()


def displacement(time, record):
    wins = 0

    # a = 1 mm/ms^2 => v0 = (1 mm/ms^2) * t ms => x(v0) mm
    for v in range(1, time):
        x = v * (time - v)
        if x > record:
            wins += 1

    return wins


def part1():
    times = list(map(int, lines[0].split()[1:]))
    records = list(map(int, lines[1].split()[1:]))
    total = 1

    for i in range(len(times)):
        total *= displacement(times[i], records[i])

    return total


# got lazy and didn't implement this
def jumping_binary(key, s_arr):
    k = 0
    n = len(s_arr)
    b = n // 2

    while b >= 1:
        while k + b < n and s_arr[k + b] <= key:
            k += b
        print(k, b)
        b = b // 2

    if key == s_arr[k]:
        return k
    else:
        return -1


time = int("".join(lines[0].split()[1:]))
record = int("".join(lines[1].split()[1:]))


def f(t, d):
    def g(x):
        return x * (t - x)

    low = 0
    high = t // 2

    if high * (t - high) <= d:
        return 0

    while high > low + 1:
        mid = (low + high) // 2
        if g(mid) > d:
            high = mid
        else:
            low = mid


def part2():
    time = int("".join(lines[0].split()[1:]))
    record = int("".join(lines[1].split()[1:]))

    return displacement(time, record)


print(part1())
print(part2())
