for tc in range(int(input())):
    ordered = list(input().split())  # 초기에 앉는 순서
    ordered = ordered[::-1]  # 반시계 방향으로 게임을 진행할 것이기 때문
    game = dict()
    start_order = []
    for i in range(3):  # 3가지 게임에 대한 input 받아오기
        input_list = list(input().split())
        game_num, start_person, game_num_lucky = input_list[0], input_list[1], list(input_list[2:])
        start_order.append(start_person)
        game[game_num] = game_num_lucky
    # print(ordered)  # 초기 게임 진행 순서
    # print(start_order)  # 3개의 각 게임을 시작하는 사람 순서
    # print(game)  # 게임별 벌칙 당첨자 딕셔너리

    lucky_people = []  # 벌칙 당첨자 리스트
    j = 0  # 게임을 시작하는 사람의 인덱스를 쓰기 위해 사용
    for i in game.keys():  # 게임을 순서대로 실행
        flag = 0
        idx = ordered.index(start_order[j])  # start_order 순으로 게임 시작하는 사람의 인덱스 찾기
        # print('game: ', i)
        # print(idx)
        # print(ordered)
        j += 1
        for g in range(idx, 8):
            if ordered[g] in game[i]:  # ordered[g]라는 사람이, 진행중이던 게임의 구멍 리스트에 존재한다면
                flag = 1
                lucky_people.append(ordered[g])
                ordered[g], ordered[(g+4) % 8] = ordered[(g+4) % 8], ordered[g]  # 자리 바꾸는 부분
                break  # 벌칙 당첨
        if flag:  # 이미 이번 게임의 벌칙 당첨자가 나온 경우이므로, else문을 찾을 필요가 없다.
            continue
        else:  # 아직 이번 게임의 벌칙 당첨자가 안나온 경우
            for g in range(idx):
                if ordered[g] in game[i]:  # ordered[g]라는 사람이, 진행중이던 게임의 구멍 리스트에 존재한다면
                    flag = 1
                    lucky_people.append(ordered[g])
                    ordered[g], ordered[(g+4) % 8] = ordered[(g+4) % 8], ordered[g]  # 자리 바꾸는 부분
                    break  # 벌칙 당첨
    # print(lucky_people)
    lucky_people = sorted(list(set(lucky_people)))
    # print(lucky_people)

    print(f'#{tc+1}', end=' ')
    for lp in lucky_people:
        print(lp, end=' ')
    print()