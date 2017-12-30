def solve(replacements, medicine):
    steps = 0

    while medicine != 'e':        
        for replacement in replacements:      
            lm = len(medicine)      
            lr = len(replacement[1])            
            starts = []

            for x in range(lm - lr + 1):
                if medicine[x:x + lr] == replacement[1]:
                    starts.append(x)

            if starts:
                for start in starts:
                    plausible = medicine[:start] + replacement[0] + medicine[start + lr:]
                    if plausible == 'e':
                        return steps + 1
                    if any(r[1] in plausible for r in replacements):
                        medicine = plausible
                        steps += 1
                        break         

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