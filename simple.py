#간단한 소인수분해
# T = int(input())
# for test_case in range(1,1+T):
#     N = int(input())
#     a=0
#     b=0
#     c=0
#     d=0
#     if N // 11 !=0:
#         e = N // 11
#         N = N % 11
#     elif N // 7 != 0:
#         d = N // 7
#         N = N % 7
#     elif N // 5 != 0:
#         c = N // 5
#         N = N % 5
#     elif N // 3 != 0:
#         b = N // 3
#         N = N % 3
#     else:
#         a = N // 2
#         N = N % 2
#     print(b)

divs = [2,3,5,7,11]
T = int(input())
for test_case in range(1,T+1):
    N =int(input())
    cnts = [0] *len(divs)
    for i in range(len(divs)):
        while N%divs[i] == 0:
            cnts[i] += 1
            N = N%divs[i]
    print(f'#{test_case}, *cnts')