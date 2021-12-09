import random

# TEST CASE 개수 설정
T = int(input())
for tc in range(T):   
    
    # 친구 5명
    People = [1, 2, 3, 4, 5]

    # 3사 스마트폰은 최소 1개 이상 존재
    Phone = random.sample(People, 3)
    for i in range(3):
        People.remove(Phone[i])

    # 3사 스마트폰 순서 설정
    for i in range(3):
        print(i+1, end = ' ')

        # 각 회사 스마트폰을 가진 친구 설정
        num_P = random.randint(0, len(People))
        PeopleList = random.sample(People, num_P)
        PeopleList.append(Phone[i])
        People.append(Phone[i])
        PeopleList = list(set(PeopleList))[::-1]
        k = len(PeopleList)
        for j in range(k):
            print(PeopleList[-1], end = ' ')
            People.remove(PeopleList[-1])
            PeopleList.pop()

        # 배터리 잔량 설정    
        for i in range(k):
            Battery = random.randint(0, 10)
            print(Battery*10, end = ' ')
        print()

