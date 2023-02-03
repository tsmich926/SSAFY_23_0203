#SWA 점점커지는 당근의 갯수

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1,0,-1):
        arr[i] -= arr[i-1]

    arr = arr[1:]
    arr.extend([0, 0])

    d = arr[0]
    cnt, max_v = 1, 0
    for i in range(N):
        k = arr[i]
        if (k > 0) and (k == d):
            cnt += 1
        else:
            if max_v < cnt:
                max_v = cnt
            cnt = 1
            d = arr[i+1]

    print(f'#{tc+1} {max_v}')