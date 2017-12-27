def solve(moves):    
    positions = [[0, 0], [0, 0]]
    visited = set([(0, 0)])
    robot = False

    for move in moves:
        if move == '>':
            positions[robot][1] += 1
        elif move == '<':
            positions[robot][1] -= 1
        elif move == '^':
            positions[robot][0] -= 1
        elif move == 'v':
            positions[robot][0] += 1

        visited.add(tuple(positions[robot]))
        robot = not robot

    return len(visited)

with open('input_3.txt', 'r') as f:
    print(solve(f.read().strip()))