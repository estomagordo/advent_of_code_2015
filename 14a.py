def solve(rd, time):
    reindeer = []

    for r in rd:
        line = r.split()
        reindeer.append([int(line[3]), int(line[6]), int(line[-2]), 0])

    for t in range(time):
        for r in reindeer:
            reindeertime = t % (r[1] + r[2])
            if reindeertime < r[1]:
                r[3] += r[0]

    return max(r[3] for r in reindeer)

with open('input_14.txt', 'r') as f:
    print(solve(f.readlines(), 2503))