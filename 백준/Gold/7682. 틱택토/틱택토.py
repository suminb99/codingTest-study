# 게임판의 상태가 주어지면, 그 상태가 틱택토 게임에서 발생할 수 있는 최종 상태인지를 판별하는 프로그램

def check_winner(board, ch):
    for i in range(3):
        if gameMap[i][0] ==  gameMap[i][1] ==  gameMap[i][2] == ch:
            return True
        
        if gameMap[0][i] ==  gameMap[1][i] ==  gameMap[2][i] == ch:
            return True
        
    if gameMap[0][0] == gameMap[1][1] == gameMap[2][2] == ch: 
        return True
    
    if gameMap[0][2] == gameMap[1][1] == gameMap[2][0] == ch: 
        return True
    
    return False

gameMap = []
results = []
while True:
    x = input().strip()
    if x == 'end': break

    # 게임판을 2차원 배열에 저장
    gameMap = [list(x[i:i+3]) for i in range(0, 9, 3)]

    # X, O 개수 확인
    countX = x.count('X')
    countO = x.count('O')

    # 틱택토 확인
    xWin = check_winner(gameMap, 'X')
    oWin = check_winner(gameMap, 'O')

    # 유효성 판정
    if xWin and (not oWin) and countX == countO + 1: results.append('valid') # x가 이긴 경우: x의 개수 > o의 개수
    elif (not xWin) and oWin and countX == countO: results.append('valid') # o가 이긴 경우: x의 개수 == o의 개수
    elif (not xWin) and (not oWin) and countX == 5 and countO == 4: results.append('valid') # 비긴 경우: x의 개수 == 5 and o의 개수 == 4
    else: results.append('invalid')

for r in results:
    print(r)