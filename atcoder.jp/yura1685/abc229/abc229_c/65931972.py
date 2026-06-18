N, W = map(int,input().split())
che = []
for _ in range(N):
    A, B = map(int,input().split())
    che.append((A,B))
che.sort(reverse=True)

yummy = 0
now = 0
while now < N:
    a, b = che[now]
    if b < W:
        W -= b
        yummy += a*b
    else:
        yummy += a*W
        break
    now += 1
print(yummy)