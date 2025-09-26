from collections import deque
import sys

# F: 전체 층수
# S: 현재 층수
# G: 목표 층수
# U: 위로 가는 버튼
# D: 아래로 가는 버튼
F, S, G, U, D = map(int, sys.stdin.readline().split())

visited = [False] * (F+1) # 0, 1층 ~ F층

def bfs():
    queue = deque()
    queue.append((S, 0)) # (현재 층수, 이동 횟수)

    visited[S] = True

    while queue: 
        floor, count = queue.popleft()

        if floor == G: # 목표 층수 도달
            return count
        
        else:
            up = floor + U # 현재 층에서 위로 U층 이동
            down = floor - D # 현재 층에서 아래로 D층 이동

            if up <= F and not visited[up]:
                visited[up] = True # 방문 처리
                queue.append((up, count + 1)) # 이동 횟수 +1

            if down >=1 and not visited[down]:
                visited[down] = True # 방문 처리
                queue.append((down, count + 1)) # 이동 횟수 +1

    return "use the stairs"

print(bfs())