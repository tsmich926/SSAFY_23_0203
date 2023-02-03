#SWA 삼성시의 버스노선
#함수 이용한 version
# def bujung(nosun):
#     bj_number = []
#     for i in range(nosun[0],nosun[1]+1,1): #어느 버정을 지나는가? 알려주는 함수
#         bj_number.append(i)
#     return bj_number


# T = int(input())
# for test_case in range(1,T+1):
#     N = int(input())
#     for i in range(N):
#         nosun = list(map(int,input().split()))
#         bns = bujung(nosun)
#         bj_cnt = [0] * 5001
#         for n in bns:
#             bj_cnt[int(n)] += 1
#         print(bj_cnt)


""""""""""""""""""""""""""""""""
#삼성 버스 노선
# import sys
# sys.stdin = open("","r")

T = int(input())
for test_case in range(1,T+1):
    N =int(input())

    #N번 반복하면서 노선입력,빈도수 표시
    cnts = [0] * 5001
    for _ in range(N):
        S ,E = map(int,input().split())
        for i in range(S, E+1):
            cnts[i]+=1

    P = int(input())
    alst = []
    for _ in range(P):
        P = int(input())
        alst.append(cnts[P])

    print(f'#{test_case} {alst}')

"""""""""""""""""""""""""""""""""""""
#간단한 소인수분해
divs = [2,3,5,7,11]
T = int(input())
for test_case in range(1,T+1):
    N =int(input())
    cnts = [0] *len(divs)
    for i in range(len(divs)):
        while N%divs[i] == 0:
            cnts[i] += 1
            N =N//divs[i]
    print(f'#{test_case}, *cnts')

""""""""""""""""""""""""""""""""""""""""""""
#연속한 1의 갯수

T = int(input())
for test_case in range(1,T+1):
    N =int(input())
    lst = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        if lst[i] == 0:
            cnt = 0
        else:
            cnt + 1
            if ans<cnt:
                ans = cnt
    print(f'#{test_case}, ans')