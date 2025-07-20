import sys

# 전역 변수로 그래프 선언
global graph 
graph = {}

def recursive_dfs(v, discovered=[]):
    discovered.append(v) # 노드 방문

    # 현재 노드가 graph에 없는 경우 탐색 종료
    if v not in graph: return discovered

    # 인접 노드들 방문했는지 확인
    for w in graph[v]:
        if w not in discovered: # 아직 방문하지 않았으면 재귀 호출로 방문
            discovered = recursive_dfs(w, discovered)
    return discovered

numC = int(sys.stdin.readline()) # 컴퓨터(노드)의 수 입력
numPair = int(sys.stdin.readline()) # 연결된 컴퓨터 쌍의 수

# 인접 리스트로 양방향 그래프 구성
for _ in range(numPair):
    s, d = map(int, sys.stdin.readline().split())
    if s not in graph:
        graph[s] = [d]
    else: 
        graph[s].append(d)
    
    if d not in graph:
        graph[d] = [s]
    else:
        graph[d].append(s)

infected = recursive_dfs(1) # 1번 컴퓨터를 포함하여 바이러스에 걸리게 되는 컴퓨터 탐색
print(len(infected) - 1) # 1번 컴퓨터를 제외한 감염된 컴퓨터 수 출력