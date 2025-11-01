import sys

N, D = map(int, sys.stdin.readline().split())
shortcuts = [[] for _ in range(D + 1)]

for _ in range(N):
    s, e, w = map(int, sys.stdin.readline().split())
    if e > D:          # 목적지가 고속도로 끝을 넘으면 무효
        continue
    if w >= e - s:     # 이득이 없는 지름길은 무시
        continue
    shortcuts[s].append((e, w))

INF = 10**15
dist = [INF] * (D + 1)
dist[0] = 0

for x in range(D):
    # 1km 전진
    if dist[x + 1] > dist[x] + 1:
        dist[x + 1] = dist[x] + 1
    # x에서 시작하는 지름길들
    for e, w in shortcuts[x]:
        if dist[e] > dist[x] + w:
            dist[e] = dist[x] + w

print(dist[D])