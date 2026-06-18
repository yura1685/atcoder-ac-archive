from itertools import product

N, K = map(int,input().split())
S = [input() for _ in range(N)]

P = list(product([True,False],repeat=N))

ans = 0
for p in product([True,False],repeat=N):
    if sum(p) < K:
        continue
    T = [S[i] for i in range(N) if p[i]]
    cnt = [0]*26
    for t in T:
        for tt in t:
            cnt[ord(tt)-ord('a')] += 1
    ans = max(ans,cnt.count(K))

print(ans)