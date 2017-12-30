def solve(grid, steps):
    for _ in range(steps):
        tng = []
        for y in range(100):
            tnl = []
            for x in range(100):
                alive = grid[y][x] == '#'
                alive_neighbours = 0
                for ny in range(max(0, y - 1), min(100, y + 2)):
                    for nx in range(max(0, x - 1), min(100, x + 2)):
                        if (ny != y or nx != x) and grid[ny][nx] == '#':
                            alive_neighbours += 1
                tnl.append('#' if alive_neighbours == 3 or (alive_neighbours == 2 and grid[y][x] == '#') else '.')
            tng.append(tnl)
        grid = tng

    return sum(sum(c == '#' for c in row) for row in grid)

with open('input_18.txt', 'r') as f:
    print(solve([list(line.strip()) for line in f.readlines()], 100))