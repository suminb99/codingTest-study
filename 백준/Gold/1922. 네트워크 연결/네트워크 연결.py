# 모든 컴퓨터를 연결하는데 필요한 최소비용을 구하는 프로그램

N = int(input()) # 노드 개수
M = int(input()) # 간선 개수

# root 배열, 각 노드의 부모를 저장, 처음애는 자기 자신이 부모
root = {i: i for i in range(1, N+1)} 
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append([c, a, b]) # 간선 비용, 연결하는 두 노드

def find(x):
    # x의 대표 찾기
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    # 대표 업데이트
    rx = find(x)
    ry = find(y)

    if rx < ry: # 더 작은 번호를 대표로
        root[ry] = rx
    else:
        root[rx] = ry

edges = sorted(edges) # 비용을 기준으로 오름차순 정렬
min_cost = 0

# 간선 하나씩 확인
for c, a, b in edges:
    if find(a) == find(b): # 간선이 이미 연결되어 있는 경우
        continue

    union(a, b) # 대표가 다르면 연결해주기
    min_cost += c # 비용에 추가

print(min_cost) # 비용 출력