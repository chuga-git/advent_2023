import sys
from collections import defaultdict, deque


# pad grid to avoid indexing issues
grid = open(sys.argv[1]).read().strip().splitlines()
for i in range(len(grid)):
    grid[i] = "." + grid[i] + "."
grid.insert(0, "." * len(grid[0]))
grid.append("." * len(grid[0]))


start_pos = ()

# grab start position
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == "S":
            start_pos = (row, col)
            print("Start position found at:", start_pos)
            print()

symbols = {
    "7": ((0, -1), (1, 0)),  # left down
    "|": ((-1, 0), (1, 0)),  # up down
    "F": ((0, 1), (1, 0)),  # right down
    "L": ((-1, 0), (0, 1)),  # up right
    "-": ((0, -1), (0, 1)),  # left right
    "J": ((-1, 0), (0, -1)),  # up left
}


def print_grid(pos, visited):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (row, col) in visited:
                grid[row] = (
                    grid[row][:col] + str(visited[(row, col)]) + grid[row][col + 1 :]
                )
            if (row, col) == pos:
                grid[row] = grid[row][:col] + "X" + grid[row][col + 1 :]
    print("\n".join(grid))


# snowflake function for starting point...
def check_start_neighbors(pos):
    valid_up = "|7F"
    valid_left = "-LF"
    valid_right = "-J7"
    valid_down = "|JL"
    row, col = pos
    neighbors = []

    if grid[row - 1][col] in valid_up:
        neighbors.append((row - 1, col))
    if grid[row + 1][col] in valid_down:
        neighbors.append((row + 1, col))
    if grid[row][col - 1] in valid_left:
        neighbors.append((row, col - 1))
    if grid[row][col + 1] in valid_right:
        neighbors.append((row, col + 1))

    assert len(neighbors) == 2
    return neighbors


def build_adj():
    adj = defaultdict(list)
    for row in range(len(grid)):
        for col in range(len(grid)):
            curr = grid[row][col]
            if curr == ".":
                continue
            if curr == "S":
                assert start_pos == (row, col)
                adj[(row, col)] += check_start_neighbors((row, col))
                continue

            # check valid neighbors via symbol map
            for diff in symbols[curr]:
                neighbor_pos = (diff[0] + row, diff[1] + col)
                neighbor_sym = grid[neighbor_pos[0]][neighbor_pos[1]]

                # check if either end of the potential neighbor lines up with our current diff
                # e.g.    X [-] X --- we check L top against - left/right and L right against - left/right
                #            L  X --- none of these points intersect, so they're not neighbors
                if neighbor_sym != "." and neighbor_sym != "S":
                    for n_diff in symbols[neighbor_sym]:
                        if diff[0] + n_diff[0] == 0 and diff[1] + n_diff[1] == 0:
                            # append both sides since we don't know the direction of the graph yet
                            if (row, col) not in adj[neighbor_pos]:
                                adj[neighbor_pos].append((row, col))
                            if neighbor_pos not in adj[(row, col)]:
                                adj[(row, col)].append(neighbor_pos)
    assert len(adj) != 0
    return adj


def check_x(r, c):
    if (grid[r][c - 1] == "X" and grid[r][c + 1] == "X") and (
        grid[r + 1][c] == "X" and grid[r - 1][c] == "X"
    ):
        return True
    return False


def traverse_bfs():
    q = deque()
    adj = build_adj()
    visited = [start_pos]
    distance = defaultdict(int)
    distance[start_pos] = 0
    q.append(start_pos)
    while q:
        s = q.popleft()
        for n in adj[s]:
            if n not in visited:
                visited.append(n)
                distance[n] = distance[s] + 1
                q.append(n)

    assert len(q) == 0

    loop_len = len(visited)
    double_area = 0

    for i in range(len(visited) - 1):
        y0, x0 = visited[i]
        y1, x1 = visited[i + 1]

        double_area += (y0 + y1) * (x0 - x1)
    # A = i + b/2 + h - 1

    # this doesn't work lmao
    A = (abs(double_area) + 2 - (loop_len - 1)) / 2

    print("Finished, final queue (should be empty):", q)
    print("Final visited, total length:", visited[-1], len(visited))
    print("Part 1 answer, max() distance and max_dist:", max(distance.values()))
    print("Part 2 answer(?), double A and A:", double_area, A)


traverse_bfs()
