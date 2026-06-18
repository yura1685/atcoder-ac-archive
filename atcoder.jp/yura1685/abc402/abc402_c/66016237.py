N, M = map(int,input().split())

L = [list(map(int,input().split())) for _ in range(M)]
eat = [0]*(N+1)
B = list(map(int,input().split()))
d = {}
for i in range(N):
    d[B[i]] = i+1

for l in L:
    m = 0
    for i in range(1,l[0]+1):
        m = max(d[l[i]], m)
    eat[m] += 1

ans = 0
for i in range(1,N+1):
    ans += eat[i]
    print(ans)
