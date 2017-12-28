from itertools import permutations

def solve(seatings):
    people = {}

    for seating in seatings:
        rule = seating.split()
        a = rule[0]
        b = rule[-1][:-1]

        if not a in people:
            people[a] = {}
        if not b in people:
            people[b] = {}

        sign = 1 if rule[2] == 'gain' else -1
        val = int(rule[3]) * sign
        
        people[a][b] = val

    people['me'] = {}

    for key in people.keys():
        if key != 'me':
            people['me'][key] = 0
            people[key]['me'] = 0
    
    best = -999999999

    for p in permutations(people.keys()):
        l = len(people)
        score = 0

        for x in range(l):
            score += people[p[x]][p[(x - 1) % l]]
            score += people[p[x]][p[(x + 1) % l]]

        best = max(best, score)

    return best

with open('input_13.txt', 'r') as f:
    print(solve(f.readlines()))