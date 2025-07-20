import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
global graph
graph = {}

def dfs(v, discovered=[]):
    discovered.append(v) # 노드 방문
    for w in graph[v]:
        if w not in discovered: # 아직 방문하지 않았으면 재귀 호출로 방문
            discovered = dfs(w, discovered)
    return discovered
    

def bfs(start_v):
    discovered = [start_v]
    queue = deque([start_v])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered


graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, d = map(int, sys.stdin.readline().split())
    graph[s].append(d)
    graph[d].append(s)

for i in range(1, n+1):
    graph[i].sort()

print(*dfs(v))
print(*bfs(v))

