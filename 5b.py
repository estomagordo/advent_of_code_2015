def nice(s):
    l = len(s)
    
    pairpair = False
    for x in range(l - 3):
        pair = s[x:x + 2]
        for y in range(x + 2, l):
            if s[y: y + 2] == pair:
                pairpair = True                

    if not pairpair:
        return False

    for x in range(l - 2):
        if s[x] == s[x + 2]:
            return True

    return False

def solve(strings):
    return sum(nice(s) for s in strings)

with open('input_5.txt', 'r') as f:
    print(solve(f.read().split('\n')))