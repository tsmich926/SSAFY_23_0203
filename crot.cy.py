T = int(input())
for test_case in (1, T+1):
    N = int(input())
    C = list(map(int,input().split()))
    # print(N, C)
    cnt = 1
    maxcnt = 1
    for i in range(1,len(C)):
        if C[i] - C[i-1] > 0:
            cnt += 1
        # print(cnt)
            if maxcnt < cnt:
                maxcnt = cnt
        else:
            cnt = 1
    print(f'#{test_case} {maxcnt}')
