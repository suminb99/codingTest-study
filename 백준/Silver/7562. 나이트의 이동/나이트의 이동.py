# 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어졌을 때, 각 테스트 케이스마다 
# 나이트가 최소 몇 번만에 이동할 수 있는지 출력하는 프로그램

from collections import deque

n = int(input())


directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
results = []


for _ in range(n):
    L = int(input()) # 체스판 크기
    chessMap = [ [ -1 ] * L for _ in range(L)]

    # 나이트가 현재 있는 칸
    start_x, start_y = map(int, input().split())

    # 나이트가 이동하려는 칸 (목표 지점)
    end_x, end_y = map(int, input().split())

    queue = deque([(start_x, start_y, 0)]) #
    chessMap[start_x][start_y] = 0

    # BFS 탐색
    while queue:
        x,y, distance = queue.popleft()
        
        if x == end_x and y == end_y: # 목표 지점에 도달하면
            results.append(distance)
            break

        for dx, dy in directions: # 8방향으로 나이트 이동
            nx, ny = x + dx, y + dy

            if 0 <= nx < L and 0 <= ny < L and chessMap[nx][ny] == -1: # 체스판 범위 내에 있고 방문하지 않은 칸이라면
                chessMap[nx][ny] = distance + 1 # 이동 거리 저장
                queue.append((nx, ny, distance + 1))

                
print(*results)