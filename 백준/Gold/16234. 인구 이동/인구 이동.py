from collections import deque

N, L, R = map(int, input().split()) # 땅의 크기, 인구 차이 범위 입력 받기
population = [list(map(int, input().split())) for _ in range(N)]


def bfs(i, j):
    queue = deque([(i, j)])
    union = []
    union.append((i, j)) # 연합 추가

    while queue:
        x, y = queue.popleft()
        for r, c in [(0, 1),(1, 0),(0, -1),(-1, 0)]:
            nx, ny = x + r, y + c # 이웃 나라
            if (0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0): # 인덱스 범위 및 이웃나라 방문 여부 확인
                if (L <= abs(population[nx][ny] - population[x][y]) <= R): # 연합에 속하는지 확인
                    # 속하면 방문 여부 체크 후 queue와 union에 추가
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))
    return union


day = 0
while True:
    open_borders = 0
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                union = bfs(i, j) # 인구 이동이 이루어지는 연합국 찾기
                if len(union) > 1: # 연합국의 수가 하나 이상이면
                    open_borders = 1 # 국경이 열림
                    new_population = sum(population[x][y] for x, y in union) // len(union) # 인구 이동 후 각 나라의 인구 수 계산
                    for x, y in union:
                        population[x][y] = new_population # 각 나라에 새로운 인구 수 저장
    
    if open_borders == 0: # 더 이상 국경이 열리지 않으면 break
        break

    day += 1 

print(day)