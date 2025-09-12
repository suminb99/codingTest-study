'''
1. 선 플레이어가 홀수 번째 차례, 후 플레이어가 짝수 번째 차례 진행
2. 0 ~ n-1까지 고유한 번호가 부여된 평면 상의 점 n 개가 주어진다.
3. 플레이어는 두 점을 연결하는 선분을 긋는다.
4. 이전에 그린 선분을 다시 그리는 것 X, 교차 가능
5. 사이클을 완성하는 순간 게임 종료
'''
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, sys.stdin.readline().split())
parent = [0] * n

for i in range(n):
    parent[i] = i

cycle = 0
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())

    if find_parent(parent, x) == find_parent(parent, y):
        cycle = i + 1
        break
    else:
        union_parent(parent, x, y)

print(cycle)