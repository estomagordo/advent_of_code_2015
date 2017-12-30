def solve(replacements, medicine):
    lm = len(medicine)
    found = set()

    for replacement in replacements:
        lr = len(replacement[0])

        for x in range(lm - lr + 1):
            if medicine[x: x + lr] == replacement[0]:
                found.add(medicine[:x] + replacement[1] + medicine[x + lr:])

    return len(found)

with open('input_19.txt', 'r') as f:
    replacements = []
    replacements_finished = False
    medicine = ''

    for line in f.readlines():
        if replacements_finished:
            medicine = line.strip()
        elif not line.split():
            replacements_finished = True
        else:
            replacement = line.split()
            replacements.append([replacement[0], replacement[2]])

    print(solve(replacements, medicine))