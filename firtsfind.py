#1의 개수세기
# T = int(input())
# for test_case in range(1,T+1):
#     N =int(input())
#     lst = list(map(int,input().split()))
#     ans = 0
#     cnt = 0
#     for i in range(N):
#         if lst[i] == 0:
#             cnt = 0
#         else:
#             cnt += 1
#             if ans < cnt:
#                 ans = cnt
#     print(f'#{test_case}, ans')

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    ss = input().split('0')
    answer = 0
    for s in ss:
        if len(s) > answer:
            answer = len(s)
    print(f"#{test_case} {answer}")