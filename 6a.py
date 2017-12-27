def solve(instructions):
    grid = [[0 for x in range(1000)] for y in range(1000)]

    for instruction in instructions:
        command = instruction.split()
        action = 0 if command[1] == 'off' else 1 if command[1] == 'on' else 2

        starty, startx = list(map(int, command[-3].split(',')))
        endy, endx = list(map(int, command[-1].split(',')))

        for y in range(starty, endy + 1):
            for x in range(startx, endx + 1):
                if action == 2:
                    grid[y][x] = 1 - grid[y][x]
                else:
                    grid[y][x] = action

    return sum(sum(line) for line in grid)

with open('input_6.txt', 'r') as f:
    print(solve(f.readlines()))