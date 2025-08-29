from collections import deque

N, M = map(int, input().split())

# 인접 리스트
record = [[] for _ in range(N+1)]

# 각 유저의 케빈 베이커의 수를 담을 배열
kevin_bakers = []

def bfs(start):
    k = [0] * (N+1) # 최단 거리 저장 배열
    visited = [start]
    queue = deque()
    queue.append(start)

    # bfs 순회
    while queue:
        current = queue.popleft()
        for adj in record[current]:
            if adj not in visited:
                k[adj] = k[current] + 1
                visited.append(adj)
                queue.append(adj)

    return sum(k) # 최단 거리 합 == start의 케빈 베이커의 수

# 양방향 그래프 인접 리스트
for _ in range(M):
    a, b = map(int, input().split())
    record[a].append(b)
    record[b].append(a)

for n in range(1, N+1):
    kevin_bakers.append(bfs(n))

print(kevin_bakers.index(min(kevin_bakers)) + 1) # 가장 작은 케빈 베이커의 수를 가진 유저의 번호 출력
