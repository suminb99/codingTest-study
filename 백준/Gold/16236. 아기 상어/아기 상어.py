from collections import deque

# BFS를 이용해 최단 거리로 먹을 수 있는 물고기를 찾기
def hunt_fish(start_i, start_j, shark_size, n, sea_map):
    visited = [[False] * n for _ in range(n)]
    queue = deque([(start_i, start_j, 0)])  # (i, j, distance)
    visited[start_i][start_j] = True
    fish_list = []

    # 상어가 먹을 수 있는 물고기를 찾음
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 방향
    while queue:
        i, j, dist = queue.popleft()

        # 먹을 수 있는 물고기를 발견
        if 0 < sea_map[i][j] < shark_size:
            fish_list.append((dist, i, j))
        
        # 네 방향으로 탐색
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and sea_map[ni][nj] <= shark_size:
                visited[ni][nj] = True
                queue.append((ni, nj, dist + 1))

    # 물고기들이 있을 경우, 가장 가까운 물고기 우선
    if fish_list:
        fish_list.sort(key=lambda x: (x[0], x[1], x[2]))  # (거리, 위쪽, 왼쪽) 순으로 정렬
        return fish_list[0]  # (거리, i, j) 반환
    return None

n = int(input())
sea_map = [list(map(int, input().split())) for _ in range(n)]

# 초기 상어 위치와 상태
time = 0
shark_size = 2
eaten_fish = 0
shark_pos = None

# 상어 위치 찾기
for i in range(n):
    for j in range(n):
        if sea_map[i][j] == 9:
            shark_pos = (i, j)
            sea_map[i][j] = 0  # 상어 위치는 0으로 바꿔줌

# 물고기 먹는 과정
while True:
    fish = hunt_fish(shark_pos[0], shark_pos[1], shark_size, n, sea_map)
    
    if fish is None:  # 먹을 수 있는 물고기가 없으면 종료
        break

    dist, i, j = fish
    time += dist  # 물고기까지 가는 시간 더하기
    sea_map[i][j] = 0  # 물고기 먹기
    shark_pos = (i, j)  # 상어 위치 업데이트
    eaten_fish += 1

    # 상어의 크기가 커지면
    if eaten_fish == shark_size:
        shark_size += 1
        eaten_fish = 0

print(time)
