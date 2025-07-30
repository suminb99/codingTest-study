# 문제: 트리의 루트를 1이라고 가정하고, 2~n번 노드의 부모를 구하는 프로그램

def find_parent_bfs(start_node):
    discovered = {start_node: 0} # 방문한 노드
    queue = [start_node]
    while queue:
        visited_node = queue.pop(0)
        for adjacent_node in tree_list[visited_node]:
            if adjacent_node not in discovered:
                discovered[adjacent_node] = visited_node # 현재 노드 : 현재 노드의 부모 저장
                queue.append(adjacent_node)
    return discovered

# 입력 1
n = int(input()) # 노드의 개수

tree_list = [[] for _ in range(n+1)]

# 입력 2: 트리 상에서 연결된 두 정점 n-1개
for _ in range(n-1):
    first, second = map(int, input().split())
    # 양방향 인접 행렬
    tree_list[first].append(second)
    tree_list[second].append(first)

node_arranged = find_parent_bfs(1)

for node in range(2, n+1):
    print(node_arranged[node]) # 2번 노드부터 순서대로 부모 노드 출력
