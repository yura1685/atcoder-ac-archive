from collections import defaultdict

H, W, N = map(int,input().split())
card = []
Xs, Ys = [], []

for _ in range(N):
    A, B = map(int,input().split())
    card.append((A,B))
    Xs.append(A)
    Ys.append(B)

Xs = sorted(set(Xs))
Ys = sorted(set(Ys))

dx, dy = defaultdict(int), defaultdict(int)

cnt = 1
for x in Xs:
    dx[x] = cnt
    cnt += 1

cnt = 1
for y in Ys:
    dy[y] = cnt
    cnt += 1

for a, b in card:
    print(dx[a], dy[b])