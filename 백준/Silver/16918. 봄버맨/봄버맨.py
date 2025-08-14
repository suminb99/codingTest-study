import sys

R, C, N = map(int, sys.stdin.readline().split())
grid = [ list(sys.stdin.readline().strip()) for _ in range(R) ]

'''
1. 초기 폭탄을 설치해 놓음
2. 1초 동안 아무것도 하지 않음 - 1초 
3. 폭탄이 설치되어 있지 않은 모든 칸에 폭탄 설치 - 1초 소비
4. 3초 전에 설치해 놓은 모든 폭탄 폭발 - 1초
5. 3, 4 반복
'''


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(bombed):
    while bombed:
        x, y = bombed.pop(0)
        grid[x][y] = '.' # 폭탄이 있는 칸 파괴
        for i, j in directions:
            nx, ny = i+x, j+y
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 'O': # 인접한 네칸 파괴
                grid[nx][ny] = '.'


bombed = []
N -= 1
while True:
    if (N <= 0):
        break

    for r in range(R):
        for c in range(C):
            if grid[r][c] == '.': # 폭탄 설치
                grid[r][c] = 'O'
            else:
                bombed.append((r, c)) # 1초 뒤 터저야 되는 폭탄 위치 저장
    N -= 1
    if (N <= 0):
        break

    bfs(bombed) # 폭탄 폭발
    N -= 1
    if (N <= 0):
        break

for row in grid:
        print(''.join(row))