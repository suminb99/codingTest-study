# 마인크래프트
import sys

n, m, b = map(int, sys.stdin.readline().split())
ground = []

for i in range(n):
    ground.append(list(map(int, sys.stdin.readline().split())))

min_time = int(1e9)
height = 0

for target in range(257):
    saveInventory = 0
    removeInventory = 0
    for y in range(n):
        for x in range(m):
            if (ground[y][x] > target): # 현재 땅의 높이가 목표보다 높을 때
                saveInventory += (ground[y][x] - target)
            else: # 현재 땅의 높이가 목표보다 낮을 때
                removeInventory += target - ground[y][x]
    
    if removeInventory > saveInventory + b: # 인벤토리의 블록 수가 음수면 건너뛰기
        continue

    time = saveInventory * 2 + removeInventory # 목표 높이로 땅을 맞추는데 걸리는 총 시간 계산
    if time <= min_time:
        min_time = time
        height = target

print(min_time, height)