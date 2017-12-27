def solve(parens):
    return parens.count('(') - parens.count(')')

with open('input_1.txt', 'r') as f:
    parens = f.read().strip()
    print(solve(parens))