import copy, sys
sys.setrecursionlimit(10**6)

def count_safe_zone(area, n, height):
    def dfs(c, r):
        if (c < 0 or r < 0 or c > n-1 or r > n-1 or area[c][r] <= height):
            return
    
        area[c][r] = 0

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
area = [list(map(int, input().split())) for _ in range(n)]

heights = set.union(*map(set, area))
safe_zone_list = []

for height in heights:
    area_d = copy.deepcopy(area)
    safe_zone_list.append(count_safe_zone(area_d, n, height))

if (max(safe_zone_list) == 0): print(1)
else: print(max(safe_zone_list))