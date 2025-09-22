'''
L - 커서 왼쪽으로 이동
D - 커서 오른쪽으로 이동
B - 커서 왼쪽 문자 삭제
P $ - $라는 문자 커서 왼쪽에 추가
'''
from collections import deque
import sys
# cursor를 기준으로 left, right 리스트로 나누기
left = deque(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline())
right = deque()

for _ in range(N):
    command = sys.stdin.readline().rstrip()

    if command == "L":
        if left:
            right.appendleft(left.pop()) # 커서가 한 칸 왼쪽으로 이동, left의 마지막 문자를 right로 이동

    elif command == "D":
        if right:
            left.append(right.popleft()) # 커서가 한 칸 오른쪽으로 이동, right의 첫 문자를 left로 이동

    elif command == "B":
        if left:
            left.pop() # 커서 왼쪽 문자 삭제

    else: 
        _, ch = command.split()
        left.append(ch) # 커서 왼쪽에 문자 삽입

print(''.join(left + right))

# text = input().rstrip()
# N = int(input())
# text_len = len(text)
# cursor = text_len

# def move_cursor_left():
#     global cursor
#     if cursor != 0:
#         cursor -= 1

# def move_cursor_right():
#     global cursor
#     if cursor != text_len:
#         cursor += 1

# for _ in range(N):
#     command = input()

#     if command == "L":
#         # cursor 왼쪽으로 이동
#         move_cursor_left()

#     elif command == "D":
#         # cursor 오른쪽으로 이동
#         move_cursor_right()
        

#     elif command == "B":
#         # cursor 왼쪽 문자 삭제
#         if cursor == 0: # 삭제할 문자 없dma
#             continue
#         text = text[:cursor-1] + text[cursor:]
#         text_len -= 1
#         move_cursor_left()

#     else:
#         # cursor 왼쪽에 문자 삽입
#         _, char = command.split()
#         text = text[:cursor] + char + text[cursor:]
#         text_len += 1
#         move_cursor_right()

# print(text)