'''
1. 선 플레이어가 홀수 번째 차례, 후 플레이어가 짝수 번째 차례 진행
2. 0 ~ n-1까지 고유한 번호가 부여된 평면 상의 점 n 개가 주어진다.
3. 플레이어는 두 점을 연결하는 선분을 긋는다.
4. 이전에 그린 선분을 다시 그리는 것 X, 교차 가능
5. 사이클을 완성하는 순간 게임 종료
'''
import sys

# 부모 루트 노드 탐색
def find_parent(parent, x):
    if parent[x] != x: # 부모가 자기 자신이 아닐 때 
        parent[x] = find_parent(parent, parent[x]) # 부모 노드 탐색
    return parent[x]

# 두 원소가 속한 집합 합치기 - 연결하기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 작은값이 부모루트가 되도록 지정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선의 개수 입력 받기
n, m = map(int, sys.stdin.readline().split())
parent = [0] * n

# 각 노드의 부모를 자기 자신으로 초기화
for i in range(n):
    parent[i] = i

cycle = 0
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())

    # 각 회차마다 싸이클 유무 판별
    if find_parent(parent, x) == find_parent(parent, y):
        cycle = i + 1 # 싸이클이 발생한 회차 저장
        break
    else:
        union_parent(parent, x, y)

print(cycle) 