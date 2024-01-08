import sys
from rich import print

raw = open(sys.argv[1]).read().strip()
sequences = [[int(x) for x in i.split()] for i in raw.splitlines()]

def predict_next(sequence):
    # initialize with first difference sequence
    diffs = [sequence] + [[sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]]
    null_set = set([0])

    # i'm pretty sure this set comparison is a crime against mathematics
    while len(null_set ^ set(diffs[-1])) != 0:
        prev_seq = diffs[-1]
        new_seq = [prev_seq[i] - prev_seq[i-1] for i in range(1, len(prev_seq))]
        diffs.append(new_seq)

    diffs.reverse()
    for s in range(len(diffs)-1):
        diffs[s+1].append(diffs[s][-1] + diffs[s+1][-1])

    # return the last value of the top sequence
    return diffs[-1][-1]

# part 2 is part 1 but in reverse
def predict_prev(sequence):
    diffs = [sequence] + [[sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]]

    null_set = set([0])

    while len(null_set ^ set(diffs[-1])) != 0:
        prev_seq = diffs[-1]
        new_seq = [prev_seq[i] - prev_seq[i-1] for i in range(1, len(prev_seq))]
        diffs.append(new_seq)

    diffs.reverse()
    for s in range(len(diffs)-1):
        # insert left most difference of first values
        diffs[s+1].insert(0, diffs[s+1][0] - diffs[s][0])

    return diffs[-1][0]

def part_1():
    predictions = []
    for s in sequences:
        predictions.append(predict_next(s))
    answer = sum(predictions)

    print("Part 1 answer:", answer)

def part_2():
    predictions = []
    for s in sequences:
        predictions.append(predict_prev(s))
    answer = sum(predictions)

    print("Part 2 answer:", answer)

part_1()
part_2()