# 4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747 774 777
# 1, 2, 1+1 1+2 2+1 2+2 1+1+1
# 1 2 3 4 5 6 7
# 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3
# 2^1 2^2 2^3
# 2 4 8 16

k = int(input())
answer = ''

while k > 0:
    remainder = k % 2 # 짝수 홀수 확인
    k = k // 2

    if remainder == 0: # 순서가 짝수일 때 숫자는 홀수, 홀수일 때 짝수
        k -= 1
        answer = '7' + answer
    else:
        answer = '4' + answer

print(int(answer))