# 정사각형 모양의 지도가 있음, 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타냄
# 연결된 여러개의 집은 하나의 단지를 이룸
# 총 단지수와 각 단지에 속하는 집의 수를 오름차순으로 정렬 후 출력

def dfs(c, r, n, h):
    if (r < 0 or c < 0 or r > n-1 or c > n-1 or complex[c][r] == '0'):
        h = 0  # 인덱스 범위 밖 or 집이 없으면 h = 0
        return 0
    
    complex[c][r] = '0'
    h = 1 # 집이 발견되면 h = 1

    # h의 값을 더해나감 (집의 수 누적)
    h += dfs(c+1, r, n, h)
    h += dfs(c-1, r, n, h)
    h += dfs(c, r+1, n, h)
    h += dfs(c, r-1, n, h)

    return h # 집의 수 반환

n = int(input()) # 지도의 가로, 세로 사이즈 (정사각형)
complex = [list(input()) for _ in range(n)] # 지도


count_complex = 0
complex_list = []
for c in range(n):
    for r in range(n):
        if complex[c][r] == '1':
            h = 0  
            count_house = dfs(c, r, n, h) # 단지 내 집의 수 저장
            count_complex += 1 # 단지 수 업데이트
            complex_list.append(count_house) # count_house 배열에 저장


complex_list.sort() # 단지 내 집의 수 오름차순으로 정렬
print(count_complex) # 단지수 출력
for i in range(count_complex):
    print(complex_list[i]) # 집의 수 출력