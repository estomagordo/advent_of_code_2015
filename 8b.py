def solve(strings):
    count = 0

    for s in strings:
        count += 4
        x = 0
        while x < len(s):
            if s[x] == '\\':
                if s[x + 1] == '\\' or s[x + 1] == '\"':
                    x += 1
                    count += 2
                elif s[x + 1] == 'x':
                    x += 3
                    count += 1
            x += 1
            
    return count

with open('input_8.txt', 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]
    print(solve(lines))