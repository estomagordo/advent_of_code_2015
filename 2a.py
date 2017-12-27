def count(line):
    a, b, c = sorted(list(map(int, line.split('x'))))
    return 2 * (a * b + a * c + b * c) + a * b

def solve(lines):
    return sum(count(line) for line in lines)

with open('input_2.txt', 'r') as f:
    print(solve(f.readlines()))