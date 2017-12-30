from itertools import combinations
from copy import copy

def fight(player, boss):
    moves = 0

    while player[0] > 0 and boss[0] > 0:
        damage = [player, boss][moves % 2][1]
        armour = [boss, player][moves % 2][2]
        deals = max(1, damage - armour)
        [boss, player][moves % 2][0] -= deals
        moves += 1

    return moves % 2
        

def solve(boss):
    swords = ((8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0))
    armours = ((0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5))
    rings = ((25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3))

    gold = 8

    while True:
        for sword in swords:
            if sword[0] > gold:
                break
            for armour in armours:
                if sword[0] + armour[0] > gold:
                    break
                if fight([100, sword[1], armour[2]], copy(boss)):
                    return gold
                for ring in rings:
                    if sword[0] + armour[0] + ring[0] > gold:
                        continue
                    if fight([100, sword[1] + ring[1], armour[2] + ring[2]], copy(boss)):
                        return gold
                for ringpair in combinations(rings, 2):
                    if sword[0] + armour[0] + ringpair[0][0] + ringpair[1][0] > gold:
                        continue
                    if fight([100, sword[1] + ringpair[0][1] + ringpair[1][1], armour[2] + ringpair[0][2] + ringpair[1][2]], copy(boss)):
                        return gold

        gold += 1

with open('input_21.txt', 'r') as f:
    boss = [int(line.split()[-1]) for line in f]
    print(solve(boss))