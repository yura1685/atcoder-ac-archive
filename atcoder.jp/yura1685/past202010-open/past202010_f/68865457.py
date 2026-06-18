from collections import defaultdict

N, K = map(int,input().split())

d = defaultdict(int)
dr = defaultdict(set)

for _ in range(N):
    S = input()
    n = d[S]
    d[S] += 1
    if n: dr[n] -= {S}
    dr[n+1].add(S)

cnt = 0
L = sorted(dr.keys())
for i in range(len(L)):
    j = -i-1
    cnt += len(dr[L[j]])
    if cnt >= K:
        if len(dr[L[j]]) > 1:
            print('AMBIGUOUS')
        else:
            print(*dr[L[j]])
        break