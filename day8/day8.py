from rich import print
import math

in_path = 'day8.in'

instr = {'L': 0, 'R': 1}

visited = []

def parser():
    """generates step path and adjacency list from modified input file because I can't write parsers"""

    with open(in_path) as f_in:
        raw = f_in.read().strip().split('\n\n')
    steps = [instr[x] for x in raw[0]]
    adj = {}

    for line in raw[1].split('\n'):
        node, *neighbors = line.split()
        adj[node] = neighbors

    return steps, adj

def part_1():
    steps, adj = parser()
    answer = traverse(steps, adj, 'AAA', 'ZZZ')

    print("Part 1 answer:", answer)


def part_2():
    steps, adj = parser()

    locations = [x for x in adj if x.endswith('A')]
    periods = []
    for i in locations:
        # get the period of oscillation from each loop and take the LCM
        period = find_period(steps, adj, i)
        periods.append(period)

    answer = math.lcm(*periods)
    print("Part 2 answer:", answer)

# copypasta of traverse() for part 2
def find_period(steps, adj, loc):
    path = 0
    step = 0
    while not loc.endswith('Z'):
        loc = adj[loc][steps[step]]
        path += 1
        step = step + 1 if step != len(steps) - 1 else 0

    return path

# this doesn't do anything since brute force simulation takes too long
def eval_locations(locations):
    for i in locations:
        if i.endswith('A'):
            print(locations, i)
        if not i.endswith('Z'):
            return False
    return True

def traverse(steps, adj, start, end):
    n = start

    step = 0
    path = 0
    while not n.endswith('Z'):
        n = adj[n][steps[step]]
        path += 1
        step = step + 1 if step != len(steps) - 1 else 0

    return path

part_1()
part_2()