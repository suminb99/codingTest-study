import sys
from collections import Counter

N = int(sys.stdin.readline())
first = sys.stdin.readline().rstrip() # 첫번째 단어
first_count = Counter(first) # Counter: 각 문자가 문자열에서 몇번씩 나타나는지 알려주는 함수

count = 0
for _ in range(N-1):
    word = sys.stdin.readline().rstrip()
    word_count = Counter(word)

    # 두 단어의 차이 계산
    diff = 0
    for ch in set(first + word): # 두 단어에 등장하는 모든 글자
        diff += abs(first_count[ch] - word_count[ch]) # 갯수의 차이 저장

    if diff <= 1: # 같은 구성 or 추가/삭제 연산으로 맞출 수 있음
        count += 1

    elif diff == 2 and len(first) == len(word): #서로 다른 한 글자만 바꾸면 맞출 수 있음 (예: DOG, DOH)
        count += 1

print(count)