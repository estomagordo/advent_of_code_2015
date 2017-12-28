sought = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

def solve(sues):
    for sue in sues:
        data = sue.split()
        number = int(data[1][:-1])
        valid = True

        for x in range(2, len(data), 2):
            parameter = data[x][:-1]
            amount = int(data[x + 1].strip(','))

            if parameter in ['cats', 'trees']:
                if amount <= sought[parameter]:
                    valid = False
                    break
            elif parameter in ['pomeranians', 'goldfish']:
                if amount >= sought[parameter]:
                    valid = False
                    break
            elif amount != sought[parameter]:
                valid = False
                break

        if valid:
            return number

with open('input_16.txt', 'r') as f:
    print(solve(f.readlines()))