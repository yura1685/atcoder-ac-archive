N, S, K = map(int,input().split())
money = 0
for i in range(N):
    P, Q = map(int,input().split())
    money += P * Q
if money < S:
    print(money + K)
else:
    print(money)