T = int(input())
for tc in range(T):
    
    # 2차원 배열로 입력받기
    arr = [list(map(int, input().split())) for _ in range(3)]

    # 0 -> 100퍼가 되기위한 각 회사별 소요시간
    charge_time = [120, 180, 150]

    # 문제 해결에서 필요없는 회사 index 삭제
    for i in range(3):
        arr[i].pop(0)

        # 문제 해결에서 필요없는 사람 index 삭제
        for j in range(int(len(arr[i])/2)):
            arr[i].pop(0)
    
    # 일반 충전기로 1개로 모든 휴대폰을 충전하는데 걸리는 시간
    charges = []
    for i in range(3):
        for j in range(len(arr[i])):
            need_charge = int((100 - arr[i][j]) * charge_time[i] / 100)
            charges.append(need_charge)
    
    # 일반충전기그룹으로 나눠질 수 있는 모든 경우의 수
    combi_list = []

    def combi(n, ans):
        if n == len(charges):
            temp = [i for i in ans]
            combi_list.append(temp)
            return
        ans.append(charges[n])
        combi(n + 1, ans)
        ans.pop()
        combi(n + 1, ans)

    combi(0, [])

    # 충전시간의 합 계산 및 중복 제거
    sum_list = []

    for i in range(len(combi_list)):
        for j in range(len(combi_list[i])):
            sum_list.append(sum(combi_list[i]))
    sum_list = sorted(list(set(sum_list)))
    # 모두 100퍼인 경우
    if len(sum_list) == 1 and sum_list[0] == 0:
        print(f'#{tc+1} {0}')
    else:
        # 일반 충전기에 들어갈 1/3 값과 가장 유사한 값 찾기
        for i in range(len(sum_list)):
            if sum_list[i] > sum(charges) / 3:
                if sum_list[i] - (sum(charges) / 3) <= ((sum(charges) / 3) - sum_list[i-1])/2:
                    print(f'#{tc+1} {int(sum_list[i])}')
                    break
                else:
                    print(f'#{tc+1} {int((sum(charges) - sum_list[i-1]) / 2)}')
                    break