from math import isqrt

N = int(input())
P = []
W = 0
for i in range(1, N+1):
    X, Y = map(int, input().split())
    P.append((X, Y, i))
    W = max(W, X)
B = W // isqrt(N) + 1

Block = [[] for _ in range(W // B + 1)]
for x, y, i in P:
    Block[x // B].append((x, y, i))

for i, L in enumerate(Block):
    L.sort(key=lambda x: x[1], reverse= (i % 2 == 1))

ans = [1]
for L in Block:
    for x in L:
        if x[2] == 1: continue
        ans.append(x[2])

print(*ans)