def count(line):
    a, b, c = sorted(list(map(int, line.split('x'))))
    return 2 * a + 2 * b + a * b * c

def solve(lines):
    return sum(count(line) for line in lines)

with open('input_2.txt', 'r') as f:
    print(solve(f.readlines()))