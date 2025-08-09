from collections import deque

M, N = map(int, input().split())
tomatoMap = []

for _ in range(N):
    tomatoMap.append(list(map(int, input().split())))

ripe = deque([])
for n in range(N):
    for m in range(M):
        if tomatoMap[n][m] == 1: # 익은 토마토의 위치 저장
            ripe.append((n, m, 0))


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 4방향

days = 0

# BFS 탐색
while ripe:
    x, y, day = ripe.popleft()

    days = max(days, day) # 익는데 가장 오래 걸린 일수 추적

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and tomatoMap[nx][ny] == 0: # 인접한 토마토들 익히기
            tomatoMap[nx][ny] = 1 
            ripe.append((nx, ny, day + 1))

    
# 모든 토마토가 익었는지 확인하기
for row in tomatoMap:
    if 0 in row:  # 익지 않은 토마토가 있으면
        print(-1)
        break
else:
    print(days)
