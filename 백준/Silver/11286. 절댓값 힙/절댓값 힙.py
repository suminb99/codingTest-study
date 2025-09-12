'''
x == 0: 배열에 x라는 값을 넣는(추가하는) 연산
x != 0: 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 연산 수행
'''

import sys
import heapq

n = int(sys.stdin.readline())
heap = [] # 힙 리스트

for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(heap, (abs(x), x)) # 힙 삽입

    else:
        if len(heap) > 0:
            node = heapq.heappop(heap) # 힙에서 최솟값 가져오기
            print(node[1]) # tuple의 2번째 원소 출력
        else:
            print(0) # 리스트가 비어있으면 0 출력