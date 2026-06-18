from itertools import product

N, X = map(int,input().split())

ball = []
for _ in range(N):
    B = list(map(int,input().split()))
    ball.append(B[1:])

c = list(product(*ball))

ans = 0
for p in c:
    h = 1
    for a in p:
        h *= a
    if h == X:
        ans += 1

print(ans)