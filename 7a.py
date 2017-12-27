def solve(instructions):
    wires = {}
    
    while True:
        for instruction in instructions:
            command = instruction.split()
            target = command[-1]
            if len(command) == 3:
                if not command[0][-1].isdigit() and not command[0] in wires:
                    continue
                val = int(command[0]) if command[0][-1].isdigit() else wires[command[0]]
                wires[command[2]] = val
            elif command[0] == 'NOT':
                if not command[1] in wires:
                    continue
                wires[target] = (~wires[command[1]] & 0xffff)
            elif command[1] == 'LSHIFT':
                if not command[0] in wires:
                    continue
                if not target in wires:
                    wires[target] = 0
                val = int(command[2])
                wires[target] = wires[command[0]] << val
            elif command[1] == 'RSHIFT':
                if not command[0] in wires:
                    continue
                if not target in wires:
                    wires[target] = 0
                val = int(command[2])
                wires[target] = wires[command[0]] >> val
            else:
                if (not command[0][-1].isdigit() and not command[0] in wires) or (not command[2][-1].isdigit() and not command[2] in wires):
                    unset = True
                    continue

                a = int(command[0]) if command[0][-1].isdigit() else wires[command[0]]
                b = int(command[2]) if command[2][-1].isdigit() else wires[command[2]]

                if command[1] == 'AND':
                    wires[target] = a & b
                elif command[1] == 'OR':
                    wires[target] = a | b

        if 'a' in wires:
            return wires['a']
 
with open('input_7.txt', 'r') as f:
    print(solve(f.readlines()))