# 지역의 높이 정보가 2차원 배열로 주어졌을 때 비의 양보다 더 높아 장마철에 물에 잠기지 않는
# 안전한 영역의 최대 개수를 계산

import copy, sys
sys.setrecursionlimit(10**6)

# dfs로 높이마다 안전한 영역의 개수를 찾는다
def count_safe_zone(area, n, height):
    def dfs(c, r):
        if (c < 0 or r < 0 or c > n-1 or r > n-1 or area[c][r] <= height): # 주어진 높이 이하의 건물은 침수
            return
    
        area[c][r] = 0 # 안전한 영역 표시

        # 상, 하, 좌, 우로 안전한 영역이 어디까지 이어지는지 확인
        dfs(c+1, r)
        dfs(c-1, r)
        dfs(c, r+1)
        dfs(c, r-1)

    count = 0
    for c in range(n):
        for r in range(n):
            if (area[c][r] > height):
                dfs(c, r)
                count += 1

    return count

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)] # 지역의 높이 정보

heights = set.union(*map(set, area)) # 높이 정보를 set에 저장 (중복 제거)
safe_zone_list = [] 

for height in heights:
    area_d = copy.deepcopy(area)
    # 비의 양을 빌딩의 높이로 두었을 때 안전한 영역의 수 계산
    safe_zone_list.append(count_safe_zone(area_d, n, height)) # 안전한 영역의 수 저장

if (max(safe_zone_list) == 0): print(1) # 모든 지역의 높이가 같을 때 1 출력
else: print(max(safe_zone_list)) # 안전한 영역의 최대 개수 출력