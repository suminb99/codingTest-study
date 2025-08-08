# 다리의 길이와 다리의 최대하중, 그리고 다리를 건너려는 트럭들의 무게가 순서대로 주어졌을 때, 
# 모든 트럭이 다리를 건너는 최단시간을 구하는 프로그램

from collections import deque

n, w, L = map(int, input().split()) # 트럭의 수, 다리의 길이, 다리의 최대하중
trucks = list(map(int, input().split()))


on_bridge = deque([]) # 다리를 건너는 트럭의 이동 현황을 track
weights = deque([]) # 현재 다리를 건너는 트럭의 무게를 저장
time = 0

weight = 0
while (trucks or on_bridge): # 건너갈 트럭이 남았거나 트럭이 다리는 건너는 중이면 true
    time += 1

    if (on_bridge): # 현재 다리를 건너는 트럭이 있으면
        for i in range(len(on_bridge)):
            on_bridge[i] -= 1 # 트럭 이동
        
        if not on_bridge[0]: # 다리를 다 건넜으면
            on_bridge.popleft() 
            weights.popleft()
            weight = sum(weights) # 다리 위의 트럭들의 무게의 합 다시 계산
    
    if (trucks): # 아직 다리를 건너지 않은 트럭이 있는 경우
        if (trucks[0] + weight <= L): # 최대하중 넘는지 체크 (다음 트럭이 다리에 올라갈 수 있는지)
            truck = trucks.pop(0)
            on_bridge.append(w) # 다리의 길이를 저장 (이동해야 되는 거리 저장) 
            weights.append(truck) # 트럭의 무게 추가
            weight = sum(weights) # 다리 위의 트럭들의 무게의 합 계산

print(time)