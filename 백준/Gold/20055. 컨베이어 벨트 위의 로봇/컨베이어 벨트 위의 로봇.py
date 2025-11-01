import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
A = deque(map(int, input().split()))  
robots = deque([False] * N)           
step = 0

zero_cnt = sum(1 for x in A if x == 0)

while zero_cnt < K:
    step += 1

    # 벨트와 로봇 함께 회전
    A.rotate(1)
    robots.rotate(1)
    robots[-1] = False  # 내리는 위치에서 로봇 즉시 하차

    # 먼저 올라간 로봇부터 이동 (오른쪽 끝에서 왼쪽으로 확인)
    for i in range(N - 2, -1, -1):
        if robots[i] and not robots[i + 1] and A[i + 1] > 0:
            robots[i] = False
            robots[i + 1] = True
            A[i + 1] -= 1
            if A[i + 1] == 0:
                zero_cnt += 1
    robots[-1] = False  # 이동 후에도 내리는 위치면 하차

    # 올리는 위치에 로봇 올리기
    if A[0] > 0 and not robots[0]:
        robots[0] = True
        A[0] -= 1
        if A[0] == 0:
            zero_cnt += 1

    # 4) 내구도 0인 칸이 K개 이상이면 종료

print(step)