def solve(containers, litres):
    counts = {}
    l = len(containers)

    for x in range(2**l):
        volume = 0
        used = 0
        
        for y in range(l):
            if 2**y & x == 2**y:
                volume += containers[y]
                used += 1

        if volume == litres:
            if not used in counts:
                counts[used] = 0
            counts[used] += 1
            
    return counts[min(counts.keys())]

with open('input_17.txt', 'r') as f:
    print(solve(list(map(int, f.readlines())), 150))