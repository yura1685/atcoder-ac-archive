N, M = map(int,input().split())

cd = [i for i in range(N+1)]

for _ in range(M):
    n = int(input())
    p = cd.index(n)
    cd[0], cd[p] = cd[p], cd[0]

for i in range(1,N+1):
    print(cd[i])