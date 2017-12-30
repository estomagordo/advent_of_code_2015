def solve(containers, litres):
    count = 0
    l = len(containers)

    for x in range(2**l):
        volume = 0
        
        for y in range(l):
            if 2**y & x == 2**y:
                volume += containers[y]

        if volume == litres:
            count += 1

    return count

with open('input_17.txt', 'r') as f:
    print(solve(list(map(int, f.readlines())), 150))