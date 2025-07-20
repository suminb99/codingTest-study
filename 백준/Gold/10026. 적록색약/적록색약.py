import sys
sys.setrecursionlimit(10**6)

def countColors(g, n):
    def dfs(y, x, ch):
            if y < 0 or y >= len(g) or x < 0 or x >= len(g[0]) or g[y][x] != ch:
                return
            g[y][x] = "-"
            dfs(y + 1, x, ch)
            dfs(y - 1, x, ch)
            dfs(y, x + 1, ch)
            dfs(y, x - 1, ch)

    count = 0
    for y in range(n):
        for x in range(n):
            ch = g[y][x]
            if (ch != "-"):
                dfs(y, x, ch)
                count += 1
    return count
    

graph = []
n = int(sys.stdin.readline())
graph_cb = [[] for _ in range(n)]
for _ in range(n):
   graph.append(list(sys.stdin.readline().strip()))

for y in range(n):
     for x in range(n):
        if (graph[y][x] == 'G'):
            graph_cb[y].append('R')
            continue
        graph_cb[y].append(graph[y][x])

print(countColors(graph, n), countColors(graph_cb, n))