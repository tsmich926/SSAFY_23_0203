#삼성버스 swa

# def bujung(nosun):
#     bj_number = []
#     for i in range(nosun[0],nosun[1]+1,1): # 쓸모x 어느 버정을 지나는가? 알려주는 함수
#         bj_number.append(i)
#     return bj_number


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    bj_cnt = [0] * 5001
    for i in range(N):
        nosun = list(map(int,input().split()))
        for i in range(nosun[0], nosun[1]+1):
            bj_cnt[i] += 1
        # print(bj_cnt)

    P = int(input())
    print(f'#{test_case}', end=' ')
    for m in range(1,P+1):
        print(bj_cnt[m], end=' ')

    print()  #다음 test_case 를 대비해 입력커서를 다음칸으로 내림

    #한 줄에 여러 개의 값을 출력하고 싶을 경우"end"를 활용하자
    #print(값, end='문자 또는 문자열')