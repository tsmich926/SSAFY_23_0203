#SWA 간단한 소인수분해

divs = [2,3,5,7,11]
T = int(input())
for test_case in range(1,T+1):
    N =int(input())
    cnts = [0] *5
    for i in range(5):
        while N%divs[i] == 0:
            cnts[i] += 1
            N = N // divs[i]
    print(f'#{test_case}',  end =" ")
    print(*cnts,  end =" ")
    print()