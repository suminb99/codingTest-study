from itertools import permutations

qn = int(input())
nums = list(range(1, 10))
num_pool = [ n for n in permutations(nums, r=3) ] # 가능성 있는 모든 조합 

for q in range(qn):
    num, strike, ball = map(int, input().split())
    str_num = str(num)

    possible_numbers = []
    for p_num in num_pool: # 후보군의 모든 숫자를 하나씩 조사
        c_strike, c_ball = 0, 0 
        for i, n in enumerate(str_num): # enumerate: index와 값을 동시에 조회할 수 있음
            if int(n) == p_num[i]: # 값, 위치가 같으면 strike
                c_strike += 1

            elif (int(n) in p_num): # 3자리 중 하나라도 값을 포함하고 있다면 ball
                c_ball += 1

        if strike == c_strike and ball == c_ball:
            possible_numbers.append(p_num)

    num_pool = possible_numbers # num_pool을 possible_number로 업데이트, 후보군 좁히기

print(len(possible_numbers))
