from collections import defaultdict

H, W = map(int,input().split())
P = [list(map(int,input().split())) for _ in range(H)]

ans = 1
for i in range(1, 1 << H):
    L = []
    for bit in range(H):
        if (i >> bit) & 1:
            L.append(P[bit])
    n = i.bit_count()
    cnt = defaultdict(int)
    for j in range(W):
        if all([L[k][j] == L[k+1][j] for k in range(n-1)]):
            cnt[L[0][j]] += 1
    if cnt:
        ans = max(ans, n * max(cnt.values()))

print(ans)