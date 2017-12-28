from re import compile, finditer

def solve(json):
    pattern = compile('[+-]?\d+(?:\.\d+)?')
    total = 0
    return sum(map(lambda match: int(match.group()), finditer(pattern, json)))

with open('input_12.txt', 'r') as f:
    print(solve(f.read().strip()))