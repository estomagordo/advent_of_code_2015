vowels = 'aeiou'
naughty = ['ab', 'cd', 'pq', 'xy']

def nice(s):
    vowelcount = sum(c in vowels for c in s)

    if vowelcount < 3:
        return False

    double = False
    fugly = False
    for x in range(len(s) - 1):
        if s[x] == s[x + 1]:
            double = True
        if s[x] + s[x + 1] in naughty:
            fugly = True
            break

    return double and not fugly    

def solve(strings):
    return sum(nice(s) for s in strings)

with open('input_5.txt', 'r') as f:
    print(solve(f.read().split('\n')))