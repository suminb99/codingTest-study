'''
과일 종류가 1부터 9까지의 번호로 주어진 과일 탕후루가 있을 때, 과일의 종류를 2개 이하로 만든다. 
이 때 과일의 개수가 가장 많은 탕후루의 과일 개수를 출력하는 프로그램
'''

n = int(input())
fruits = list(map(int, input().split()))

fruit_counts = {} # 각 과일 종류의 수를 담을 딕셔너리
first = 0 # 남은 과일의 시작점
maxF = 0 # 과일의 개수가 가장 많은 탕후루의 과일 개수

for index, fruit in enumerate(fruits):

    # 과일의 개수 세기
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1

    # 탕후루에 꽂힌 과일 종류가 3개면  
    while len(fruit_counts) > 2:
        fruit_counts[fruits[first]] -= 1 # 가장 왼쪽의 과일부터 제거

        # 과일 종류가 2개가 될 때까지 제거
        if fruit_counts[fruits[first]] == 0:
            del fruit_counts[fruits[first]]

        first += 1 # 시작점 업데이트 (남은 과일 기준)

    maxF = max(maxF, index - first + 1) # 과일의 개수 업데이트

print(maxF)