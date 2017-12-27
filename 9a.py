from itertools import permutations

def solve(distances):
    graph = {}
    
    for distance in distances:
        distlist = distance.split()
        u = distlist[0]
        v = distlist[2]
        d = int( distlist[-1])

        if not u in graph:
            graph[u] = {}
        if not v in graph:
            graph[v] = {}

        graph[u][v] = d
        graph[v][u] = d

    best = 10000000

    for p in permutations(graph.keys()):
        distance = 0
        for x in range(len(p) - 1):
            distance += graph[p[x]][p[x + 1]]
        best = min(best, distance)

    return best

with open('input_9.txt', 'r') as f:
    print(solve(f.readlines()))