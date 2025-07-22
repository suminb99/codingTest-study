def countCandies(mc, n, x1, y1, x2, y2):
    mc = [row[:] for row in mc]

    maxCount = 1
    mc[x1][y1], mc[x2][y2] = mc[x2][y2], mc[x1][y1]

    # 각 행에서 연속된 사탕의 최대 길이 찾기
    for i in range(n):

        # 각 행에서 연속된 사탕의 최대 길이 찾기
        col = 1
        for j in range(1, n):
            if mc[i][j] == mc[i][j-1]:  # 연속된 사탕
                col += 1
            else:
                maxCount = max(maxCount, col)
                col = 1
        maxCount = max(maxCount, col)  # 마지막 연속된 부분도 체크

        # 각 행에서 연속된 사탕의 최대 길이 찾기
        row = 1
        for j in range(1, n):
            if mc[j][i] == mc[j-1][i]:  # 연속된 사탕
                row += 1
            else:
                maxCount = max(maxCount, row)
                row = 1
        maxCount = max(maxCount, row)  # 마지막 연속된 부분도 체크

    return maxCount

n = int(input())
m = []

for _ in range(n):
    m.append(list(input()))
    
counts = []

for i in range(n):
    for j in range(n):
        if j < n-1: 
            counts.append(countCandies(m, n, i, j, i, j+1))

        if i < n-1:
            counts.append(countCandies(m, n, i, j, i+1, j))


print(max(counts))
