#백만장자 프로젝트 swa

# 이익을 리턴해주는 함수만들기
def baeckman(prices):
    max_P = 0
    benef = 0
    for Price in Prices:
        if max_P < Price:
            max_P = Price
    idx = Prices.index(max_P)
    if idx != 0:
        PL = Prices[0:idx]
        buy = 0
        for i in PL:
            buy += i
        sell_P = Prices[idx] * idx
        benef = sell_P - buy
        return benef
    else:
        benef = 0
        return  benef

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    Prices = list(map(int,input().split()))
    while Prices == [] :
        res = baeckman(Prices)
        Prices = Prices[Prices.index(max(Prices)):]
    print(f'#{tc} {res}')

# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     Prices = list(map(int,input().split()))
#     max_P = 0
#     benef = 0
#     for Price in Prices:
#         if max_P < Price:
#             max_P = Price
#     idx = Prices.index(max_P)
#     if idx != 0:
#         PL = Prices[0:idx]
#         buy = 0
#         for i in PL:
#             buy += i
#         sell_P =Prices[idx]* idx
#         benef = sell_P - buy
#         print(benef)
#     else:
#         benef = 0

