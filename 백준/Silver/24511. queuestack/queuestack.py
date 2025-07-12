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
        queue.appendleft(dsList[i]) # 결과 리스트에 원소 저장

queue.extend(add)
output = list(queue)[:numAdd] 

print(*output) # 결과 리스트를 공백으로 구분하여 출력