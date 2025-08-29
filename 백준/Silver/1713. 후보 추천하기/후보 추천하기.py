n = int(input())
m = int(input())
voted = list(map(int, input().split()))

frames = {} # 사진틀
order = {} # 기재 순서 기록

def find_candidate_to_drop():
    min_vote = min(frames.values())
    candidates = [c for c, v in frames.items() if v == min_vote] # 가장 적은 득표 수를 받은 후보 모음

    if len(candidates) == 1:
        return candidates[0]
    
    # 가장 오래된 후보 찾기
    time = float('inf')
    oldest = -1
    for c in candidates:
        if order[c] < time:
            time = order[c]
            oldest = c

    return oldest
            

for i, vote in enumerate(voted):
    if vote in frames:
        frames[vote] += 1 # 후보가 사진틀에 기재되어 있으면 추천 수 증가

    else:
        if len(frames) == n:
            drop = find_candidate_to_drop() # 제거할 후보 찾기
            # 기록에서 제거
            del frames[drop]
            del order[drop]

        # 새로운 후보와 순서 등록
        frames[vote] = 1
        order[vote] = i

print(*sorted(frames.keys())) # 학생 번호 증가하는 순으로 출력