from collections import defaultdict

N, M = map(int,input().split())
A, B, C, D, E, F = map(int,input().split())
step = [(A,B), (C,D), (E,F)]
mod = 998244353

no = set()
for _ in range(M):
    x, y = map(int,input().split())
    no.add((x,y))

dp = defaultdict(int)
dp[(0,0)] = 1

for _ in range(N):
    new_dp = defaultdict(int)
    for (x, y), cnt in dp.items():
        for a, b in step:
            nx, ny = x + a, y + b
            if (nx,ny) in no:
                continue
            new_dp[(nx,ny)] += cnt
    for nx, ny in new_dp:
        new_dp[(nx,ny)] %= mod
    dp = new_dp

print(sum(dp.values()) % mod)