from itertools import combinations
from functools import reduce

def solve(weights):
    total_weight = sum(weights)
    front_weight = total_weight // 4
    lowest_quantum = 999999999999999

    for x in range(1, len(weights)):
        if lowest_quantum < 999999999999999:
            break
        for c in combinations(weights, x):
            if sum(c) == front_weight:
                lowest_quantum = min(lowest_quantum, reduce(lambda x, y: x * y, c))

    return lowest_quantum

with open('input_24.txt', 'r') as f:
    weights = list(map(int, f.readlines()))
    print(solve(weights))