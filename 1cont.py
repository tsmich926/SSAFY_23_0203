#SWA 연속하는 1의 개수세기
# T = int(input())
# for tc in range(1,T):
#     s = input()
#     for i in range(len(s)):
#         if s[i] == s[i+1]:
#             cnt += 2
#         elif:

#카운트 할 수 있는 값을 담을  인덱스를 만든다

#카운트 수를 비교한다음 카운트가 같으면 큰수를 낸다

T = int(input())
for tc in range(1,T):
    s = list(map(int, input()))
    arr = [0] * (max(s)+1)
