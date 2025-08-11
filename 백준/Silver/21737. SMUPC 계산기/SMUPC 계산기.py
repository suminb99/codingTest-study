# 수로 시작해서 알파벳으로 끝내기
# 수식에 음수 입력 X
# S: -
# M: *
# U: /
# P: +
# C: return

from collections import deque
import sys

n = int(sys.stdin.readline()) # 기호의 개수
exp = deque(sys.stdin.readline().strip()) # 수식

if 'C' not in exp:
    print("NO OUTPUT")
    sys.exit()

operand = deque() # 피연산자
operator = deque() # 연산자

num = '0'
for x in exp:
    if x.isdigit():
        if num == '0' and x == '0':
            continue
        num += x

    else:
        operator.append(x)
        if x == 'C': continue # 연산자가 'C'인 경우에는 피연산자 저장 X
        operand.append(int(num)) # 문자열로 된 숫자를 정수를 변환해서 operand에 저장
        num = '0' # 문자 0으로 초기화

operand.append(int(num)) # 마지막 숫자 저장

a = operand.popleft()
output = []

for i in operator:
    if i == 'C':
        output.append(a)
        continue

    b = operand.popleft()
    # 연산 수행
    if i == 'S': # -
        a -= b
    elif i == 'M': # *
        a *= b
    elif i == 'U': # //
        if a < 0: 
            a *= -1
            a //= b
            a *= -1
        else:
            a //= b
    else: # +
        a += b

print(*output)