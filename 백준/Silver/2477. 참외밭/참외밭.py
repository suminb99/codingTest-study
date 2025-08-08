n = int(input()) # 1m2의 넓이에 자라는 참외의 개수

directions = [] # 방향
lengths = [] # 길이
max_h, max_v = 0, 0

for _ in range(6):
    x, y = map(int, input().split())
    directions.append(x)
    lengths.append(y)

    if (x == 1 or x == 2) and y > max_h: # 직사각형의 가로 길이 구하기
        max_h = y

    if (x == 3 or x == 4) and y > max_v: # 직사각형의 세로 길이 구하기
        max_v = y

full_area = max_h * max_v # 모퉁이가 없다는 가정하에 직사각형의 넓이 구하기
empty_area = 0

shapes = [(1, 3), (4, 1), (2, 4), (3, 2)] # ㄱ, ㄱ-90, ㄱ-180, ㄱ-270 

for i in range(6):
    j = (i + 1) % 6
    if (directions[i], directions[j]) in shapes: # 방향 회전에 따라 빈 공간의 가로 세로 길이 구하기
        empty_area = lengths[i] * lengths[j] # 빈 공간의 넓이 구하기
        break

print((full_area-empty_area)*n) # 참외밭의 면적을 구한 후 참외 개수 곱하기
