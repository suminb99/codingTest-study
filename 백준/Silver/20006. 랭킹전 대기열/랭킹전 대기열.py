p, m = map(int, input().split()) # p: 참가자 수, m: 방의 정원
rooms = {}

order = 0
for _ in range(p):
    level, name = input().split() # 플레이어의 레벨과 이름 입력

    # 방이 없으면 새로 생성
    if not rooms:
        # 방이 꽉 찼는지 여부
        full = 0
        if m == 1: full = 1
        # (방 생성 순서, 방 기준 레벨): (방 꽉 찼는지 여부, 플레이어 리스트)
        rooms[(order, int(level))] = (full, [(name, int(level))]) 
        order += 1

    else:
        flag = False # 방 입장 여부 확인용
        for k in rooms.keys():
            if rooms[k][0] == 1: # 방이 꽉 찼으면 패스
                continue
            # 입장할 수 있는 방이 있으면 입장
            if k[1]-10 <= int(level) <= k[1]+10:
                flag = True
                rooms[k][1].append((name, int(level)))
                # 방이 꽉 찼는지 확인
                if len(rooms[k][1]) == m: 
                    rooms[k] = (1, rooms[k][1]) # 방이 꽉 찼음을 표시
                break

        if not flag:
            full = 0
            if m == 1: full = 1
            rooms[(order, int(level))] = (full, [(name, int(level))])
            order += 1


for k in sorted(rooms.keys()): # 방 생성 순서대로 출력
    if rooms[k][0] == 1:
        print("Started!")
    else:
        print("Waiting!")

    for player in sorted(rooms[k][1], key=lambda x: x[0]): # 이름순으로 정렬
        print(player[1], player[0]) # 레벨, 이름 순서로 출력