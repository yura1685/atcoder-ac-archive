from collections import deque

def f(a, b, c, d):
    m = min(a, b, c, d)
    if a == m: return min(b, c, d) + 1
    if b == m: return min(a, c, d) + 1
    if c == m: return min(a, b, d) + 1
    if d == m: return min(a, b, c) + 1

inf = 10 ** 18
I = input().split()
H, W, K = int(I[0]), int(I[1]), int(I[2])
L = [[inf] * (W + 2) for _ in range(H + 2)]
X = [[False] * (W + 2) for _ in range(H + 2)]
for _ in range(K):
    I = input().split()
    h, w = int(I[0]), int(I[1])
    L[h][w] = 0
    X[h][w] = True

d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
dq = deque()
for h in range(1, H+1):
    for w in range(1, W+1):
        if L[h][w] < inf: continue
        cnt = 0
        for dh, dw in d:
            nh, nw = h + dh, w + dw
            if L[nh][nw] < inf:
                cnt += 1
        if cnt > 1:
            dq.append((h, w))
            X[h][w] = True

while dq:
    h, w = dq.popleft()
    L[h][w] = f(L[h-1][w], L[h][w-1], L[h][w+1], L[h+1][w])
    for dh, dw in d:
        h2, w2 = h + dh, w + dw
        if L[h2][w2] < inf: continue
        if X[h2][w2]: continue
        if not (1 <= h2 <= H and 1 <= w2 <= W): continue
        cnt = 0
        for dh2, dw2 in d:
            if L[h2+dh2][w2+dw2] < inf:
                cnt += 1
        if cnt > 1:
            dq.append((h2, w2))
            X[h2][w2] = True

for h in range(H+2):
    for w in range(W+2):
        if L[h][w] == inf:
            L[h][w] = 0

ans = 0
for h in range(1, H+1):
    for w in range(1, W+1):
        ans += L[h][w] if L[h][w] < inf else 0

print(ans)