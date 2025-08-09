# 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램

n = int(input()) # 전체 사람의 수
p1, p2 = map(int, input().split()) # 촌수를 계산해야 하는 서로 다른 두 사람
m = int(input())  # 부모 자식들 간의 관계의 개수

graph = [[] for _ in range(n+1)]

for _ in range(m):
    # x는 y의 부모
    # 2차원 배열 양방향 인접 행렬
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)

def dfs(v, num):
    if v == p2: # 목표 지점에 도달하면 num을 반환 (num == 촌수))
        return num
    
    visited[v] = True # 현재 노드 방문 처리
    for w in graph[v]:
        if not visited[w]:
            result = dfs(w, num+1) # 다음 노드로 넘어갈 땐 촌수 +1
            if result != -1:
                return result  
    return -1

answer = dfs(p1, 0)
print(answer)
