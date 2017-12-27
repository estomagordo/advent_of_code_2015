def solve(moves):    
    y = 0
    x = 0
    visited = set((y, x))

    for move in moves:
        if move == '>':
            x += 1
        elif move == '<':
            x -= 1
        elif move == '^':
            y -= 1
        elif move == 'v':
            y += 1

        visited.add((y, x))

    return len(visited)

with open('input_3.txt', 'r') as f:
    print(solve(f.read().strip()))