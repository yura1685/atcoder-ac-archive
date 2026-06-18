from itertools import accumulate

N, K = map(int,input().split())
medic = [tuple(map(int,input().split())) for _ in range(N)]
medic.sort()

d = {0:0}
d_r = {0:0}
cnt = 1
rui = [0]*(N+1)

for a, b in medic:
    if d.get(a) == None:
        d[a] = cnt
        d_r[cnt] = a
        cnt += 1
    c = d[a]
    rui[0] += b
    rui[c] -= b

ans = list(accumulate(rui))
for i in range(N+1):
    if ans[i] <= K:
        print(d_r[i]+1)
        break
