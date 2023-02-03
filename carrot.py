T = int(input())
for t in range(1, T+1):
    N = int(input())
    C = list(map(int,input().split()))
    # print(N, C, T, t)
    cnt = 1
    max_cnt = 1
    for i in range(1,len(C)):
        if C[i] - C[i-1] > 0:
            cnt += 1
        # print(cnt)
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 1
    print(f'#{t} {max_cnt}')