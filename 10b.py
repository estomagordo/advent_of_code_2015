def solve(sequence):
    for _ in range(50):
        next = []

        last = sequence[0]
        lastpos = 0
        x = 1

        while x < len(sequence):
            if sequence[x] != last:
                next.append(str(x - lastpos))
                next.append(last)
                last = sequence[x]
                lastpos = x
            x += 1

        next.append(str(x - lastpos))
        next.append(last)

        sequence = ''.join(next)

    return len(sequence)

print(solve('1113122113'))