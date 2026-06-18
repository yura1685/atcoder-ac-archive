from more_itertools import distinct_permutations

N, M, Q = map(int,input().split())
X = [tuple(map(int,input().split())) for _ in range(Q)]

ans = 0
for P in distinct_permutations(['|']*N + ['o']*(M-1)):
    l = []
    cnt = 1
    for p in P:
        if p == '|':
            l.append(cnt)
        else:
            cnt += 1
    res = 0
    for a, b, c, d in X:
        if l[b-1] - l[a-1] == c:
            res += d
    ans = max(ans,res)

print(ans)