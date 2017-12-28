def score(ingredients):
    kilocalories = sum(ingredient[0] * ingredient[1][4] for ingredient in ingredients)

    if kilocalories != 500:
        return 0

    capacity = sum(ingredient[0] * ingredient[1][0] for ingredient in ingredients)
    durability = sum(ingredient[0] * ingredient[1][1] for ingredient in ingredients)
    flavour = sum(ingredient[0] * ingredient[1][2] for ingredient in ingredients)
    texture = sum(ingredient[0] * ingredient[1][3] for ingredient in ingredients)

    return max(0, capacity) * max(0, durability) * max(0, flavour) * max(0, texture)

def solve(lines, amount):
    ingredients = []

    for line in lines:
        ls = line.split()
        ingredients.append((int(ls[2][:-1]), int(ls[4][:-1]), int(ls[6][:-1]), int(ls[8][:-1]), int(ls[10])))

    best = 0

    for a in range(amount):
        for b in range(amount - a):
            for c in range(amount - a - b):
                d = amount - a - b - c
                value = score([[a, ingredients[0]], [b, ingredients[1]], [c, ingredients[2]], [d, ingredients[3]]])
                best = max(best, value)

    return best

with open('input_15.txt', 'r') as f:
    print(solve(f.readlines(), 100))