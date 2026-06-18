N, M = map(int,input().split())
sub, res, pena = [0]*N, [0]*N, [0]*N

for _ in range(M):
    p, r = map(str,input().split())
    p = int(p)
    if r == 'WA':
        sub[p-1] += 1
    else:
        if res[p-1] == 0:
            res[p-1] = 1
            pena[p-1] = sub[p-1]

print(sum(res), sum(pena))