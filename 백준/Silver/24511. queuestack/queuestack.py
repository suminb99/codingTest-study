# queuestack 문제
# n개의 자료구조가 queuestack에 나열되어 있으며, 
# 자료구조는 queue 또는 stack이며, 
# 각각의 자료구조는에는 한 개의 원소가 들어있다
# 길이 m의 수열 c를 가져와서 수열의 원소를 차례대로 queuestack에 삽입한다
# 각 자료구조는 원소가 삽입 됐을 때 pop 연산을 수행하고 마지막 자료구조의 리턴값 차례대로 저장하여 출력하면 된다.

import sys
from collections import deque

numDs = int(sys.stdin.readline()) # 자료구조 수
dsTypes = deque(map(int, sys.stdin.readline().split())) # 자료구조 구성, 0 == queue, 1 == stack
dsList = deque(map(int, sys.stdin.readline().split())) # 각 자료구조의 원소들
numAdd = int(sys.stdin.readline()) # 삽입할 원소의 개수
add = deque(map(int, sys.stdin.readline().split())) # 삽입할 원소 리스트

queue = deque()

for i in range(numDs):
    if not dsTypes[i]: # 자료구조가 queue인 경우
        queue.appendleft(dsList[i]) # 결과 리스트에 원소 저장 (가장 오래된 원소가 앞으로 오게)

queue.extend(add) # 삽입할 원소를 큐의 뒷부분에 연장
output = list(queue)[:numAdd] # 삽입한 원소의 크기만큼 가장 오래된 원소순으로 slice

print(*output) # 결과 리스트를 공백으로 구분하여 출력