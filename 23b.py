def solve(instructions):
    registers = {'a': 1, 'b': 0}
    pos = 0
    l = len(instructions)

    while 0 <= pos < l:
        instruction = instructions[pos]
        command = instruction[0]

        if command == 'hlf':
            registers[instruction[1]] //= 2
        elif command == 'tpl':
            registers[instruction[1]] *= 3
        elif command == 'inc':
            registers[instruction[1]] += 1
        elif command == 'jmp':
            pos += int(instruction[1]) - 1
        elif command == 'jie':
            if registers[instruction[1][:-1]] % 2 == 0:
                pos += int(instruction[2]) - 1
        elif command == 'jio':
            if registers[instruction[1][:-1]] == 1:
                pos += int(instruction[2]) - 1

        pos += 1

    return registers['b']

with open('input_23.txt', 'r') as f:
    instructions = [line.split() for line in f]
    print(solve(instructions))