def solve(row, column):
    diagonal = row + column - 1
    previous = ((diagonal-1) * (diagonal-1) + diagonal - 1) // 2
    steps = previous + column - 1

    val = 20151125

    for x in range(steps):
        val = (val * 252533) % 33554393

    return val

with open('input_25.txt', 'r') as f:
    line = f.readline().split()
    row = int(line[-3][:-1])
    column = int(line[-1][:-1])
    print(solve(row, column))