import random

# TEST CASE 개수 설정
T = int(input())
for tc in range(T):   

    # 앉는 순서 설정
    seat = []
    for i in range(8):
        k = random.randint(1, 8)
        while True:
            k = random.randrange(1, 9)
            if k not in seat:
                break
        seat.append(k)
    for i in seat:
        print(i, end=' ')
    print()

    # 3개의 게임 뽑기
    game_number = []
    for i in range(3):
        k = random.randint(1, 5)
        while True:
            k = random.randrange(1, 6)
            if k not in game_number:
                break
        game_number.append(k)

    # 3개의 게임 시작 친구 뽑기
    start_list = []
    for i in range(3):
        start_number = random.randint(1, 8)
        start_list.append(start_number)

    # 구멍인 친구 
    bomb_list = []
    for i in range(3):
        bomb_number = random.randint(1, 3)
        bomb = []
        for i in range(bomb_number):
            k = random.randint(1, 3)
            while True:
                k = random.randrange(1, 8)
                if k not in bomb:
                    break
            bomb.append(k)
        bomb_list.append(bomb)

    # 게임, 게임 시작 친구, 구멍인 친구 출력
    for i in range(3):
        a = game_number[i]
        b = start_list[i]
        bomb_list[i]
        print(a, b, end=' ')
        for j in bomb_list[i]:
            print(j, end= ' ')
        print()