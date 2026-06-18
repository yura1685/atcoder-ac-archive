N, K = map(int, input().split())
Q = [list(map(int, input().split())) for _ in range(N)]
l, r = 0, 100
for _ in range(100):
    mid = (l + r) / 2
    L = sorted([w * (p - mid) for w, p in Q], reverse=True)
    if sum(L[:K]) >= 0: l = mid
    else: r = mid
print(l)