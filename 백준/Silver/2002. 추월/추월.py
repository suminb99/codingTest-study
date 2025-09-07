'''
터널에 차량들이 일정한 순서로 진입하고 다시 일정한 순서로 빠져나온다.
터널 내부에서 반드시 추월 했을 것이라 판단되는 차량의 수를 출력하라.
'''

N = int(input())

enter = [] # 터널에 진입하는 차량
exit = [] # 터널에서 빠져나오는 차량

for _ in range(N):
    car = input()
    enter.append(car)

for _ in range(N):
    car = input()
    exit.append(car)

outrun = 0 # 추월한 차량의 수
for i in range(N):
    if exit[i] == enter[i]: # 진입 순서와 진출 순서가 같으면 추월 없음
        continue

    # 진출 차량의 위치를 진입 리스트에서 찾아 현재 위치로 이동
    idx = enter.index(exit[i]) # 진출 차량이 진입 리스트에서 몇 번째인지 찾음
    car = enter.pop(idx) # 해당 차량을 진입 리스트에서 꺼냄
    enter.insert(i, car) # 현재 진출 순서 위치로 삽입
    outrun += 1 # 추월 발생 -> 추월 카운트 증가

print(outrun)