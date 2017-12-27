def solve(parens):
    level = 0

    for pos, paren in enumerate(parens):
        if paren == '(':
            level += 1
        else:
            level -= 1
        
        if level == -1:
            return pos + 1

with open('input_1.txt', 'r') as f:
    parens = f.read().strip()
    print(solve(parens))