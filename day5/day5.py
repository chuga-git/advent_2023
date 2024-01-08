from rich import print

in_path = 'day5.in'

with open(in_path) as f_in:
    raw = f_in.read().strip()
    lines = raw.splitlines()

seeds, *maps = raw.split('\n\n')
seeds = [int(x) for x in seeds.split(':')[1].split()]

seed_pairs = list(zip(seeds[::2], seeds[1::2]))

maps = [[(int(i.split()[0]), int(i.split()[1]), int(i.split()[2])) for i in x.split('\n')[1:]] for x in maps]

def process_stage(seed, endpoints):
    for endpoint in endpoints:
        dest, src, rng = endpoint

        if src <= seed < src + rng:
            return dest + (seed - src)
    
    return seed

def part1():
    final_seeds = []
    for s in seeds:
        for m in maps:
            s = process_stage(s, m)
        final_seeds.append(s)
    
    print('Part 1 answer:', min(final_seeds))

# mostly grafted from Jonathan Paulson's solution
def process_ranges(seed_pair, m):
    # ranges that were successfully mapped
    trans_ranges = []

    for (dest, src, src_rng) in m:
        src_end = src + src_rng

        # store ranges that weren't successfully mapped in this pass
        unmapped = []

        # loop through each tuple in seed pair, which grows to encompass unmapped ranges
        while seed_pair:
            seed_start, seed_end = seed_pair.pop()

            # Allen's interval algebra - these rules apparently hold for all cases
            # the 'before' interval either cuts off at src or at the end of its range (in which case the ranges don't overlap)
            before_start, before_end = seed_start, min(src, seed_end) 

            # the overlap of the two intervals starts at the right-most of the start points and ends at the left-most of the end points
            overlap_start, overlap_end = max(seed_start, src), min(seed_end, src_end)

            # the 'after' interval starts at the right-most of either src_end or seed_start (which is a miss) and ends at seed_end
            after_start, after_end = max(src_end, seed_start), seed_end

            if before_end > before_start:
                unmapped.append((before_start, before_end))
            if overlap_end > overlap_start:
                # there was an intersection, so modify the endpoints
                trans_ranges.append((overlap_start - src + dest, overlap_end - src + dest))
            if after_end > after_start:
                unmapped.append((after_start, after_end))
        
        # everything that could have been transformed is now in trans_ranges, so carry over the rejects
        seed_pair = unmapped

    # anything still remaining after every pass is still a valid range
    return trans_ranges + seed_pair
        
def part2():
    final_seeds = []

    for start, rng in seed_pairs:
        # wrap as list so it can be used as a container in process_ranges()
        pair = [(start, start+rng)]

        for m in maps:
            pair = process_ranges(pair, m)

        final_seeds.append(min(pair)[0])

    print("Part 2 answer:", min(final_seeds))

part1()
part2()