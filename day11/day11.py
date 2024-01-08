import itertools

with open('day11.in') as f:
    lines = f.read().strip().splitlines()

def transpose(matrix):
    "Swap the rows and columns of a 2-D matrix."
    return [''.join(s) for s in zip(*matrix)]

def print_2d(grid):
    g = grid.copy()
    counter = 1
    for l in range(len(g)):
        for j in range(len(g[l])):
            if g[l][j] == '#':
                g[l] = g[l][:j] + str(counter) + g[l][j+1:]
                counter += 1
    for i in g:
        print(' '.join(i))
    print()

def get_pairs(g):
    # list of non repeating pairs (tuples) of galaxies -> list[tuple(tuple, tuple)]
    return list(itertools.combinations(g, 2))

def compute_lengths(pairs):
    L = []
    for pair in pairs:
        a, b = pair
        L.append(abs(a[0] - b[0]) + abs(a[1] - b[1]))
    return L

def get_galaxy_positions(img):
    positions = []
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j] == '#':
                positions.append((i, j))

    return positions

def transpose_positions(pos_list):
    for i in range(len(pos_list)):
        pos_list[i] = (pos_list[i][1], pos_list[i][0])
    return pos_list

def part_1():
    new_image = lines.copy()

    # manual fill, doesn't work for larger expansion numbers but still looks cool when printed out
    for i in range(2):
        k = 0
        while k < len(new_image):
            if '#' not in new_image[k]:
                new_image.insert(k, '.' * len(new_image[k]))
                k += 1
            k += 1

        new_image = transpose(new_image)


    galaxies = get_galaxy_positions(new_image)
    print("Part 1 answer:", sum(compute_lengths(get_pairs(galaxies))))

def part_2():

    new_image = lines.copy()

    # grab initial positions so we can offset later
    init_positions = get_galaxy_positions(new_image)
    positions = init_positions.copy()

    for i in range(2):
        offsets = []

        for i in range(len(new_image)):
            if '#' not in new_image[i]:
                offsets.append(i)
        for offset in range(len(offsets)):
            for i in range(len(init_positions)):
                row = init_positions[i][0]
                if row > offsets[offset]:
                    positions[i] = (row + ((1000000 - 1) * (offset + 1)), positions[i][1])


        transpose_positions(positions)
        transpose_positions(init_positions)
        new_image = transpose(new_image)

    print("Part 2 answer:", sum(compute_lengths(get_pairs(positions))))
    
part_1()
part_2()