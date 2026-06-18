N, Q = map(int,input().split())
A = list(map(int,input().split()))
d = {}
for i in range(N):
    a = A[i]
    if d.get(a) == None:
        d[a] = [1,i+1]
    else:
        d[a].append(i+1)
        d[a][0] += 1

for _ in range(Q):
    x, k = map(int,input().split())
    if d.get(x) == None:
        print(-1)
    else:
        n = d[x][0]
        if k > n:
            print(-1)
        else:
            print(d[x][k])