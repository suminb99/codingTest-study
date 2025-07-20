import sys
sys.setrecursionlimit(10**6)

def countCabbageFarm(cabbageMap, w, h):

    def dfs(y, x):
        if y < 0 or y >= len(cabbageMap) or x < 0 or x >= len(cabbageMap[0]) or cabbageMap[y][x] != 1:
            return
        cabbageMap[y][x] = 0
        dfs(y + 1, x)
        dfs(y - 1, x)
        dfs(y, x + 1)
        dfs(y, x - 1)
    
    count = 0
    for y in range(h):
        for x in range(w):
            if cabbageMap[y][x] == 1:
                dfs(y, x)
                count += 1
    
    return count

counts = []
numTest = int(sys.stdin.readline())

for _ in range(numTest):
    w, h, c = map(int, sys.stdin.readline().split())
    graph = [[0]*w for _ in range(h)]

    for _ in range(c):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    counts.append(countCabbageFarm(graph, w, h))

for i in range(numTest):
    print(counts[i])

