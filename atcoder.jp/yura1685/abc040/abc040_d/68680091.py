from atcoder.dsu import DSU

N, M = map(int,input().split())
X = []

for _ in range(M):
    a, b, y = map(int,input().split())
    X.append((y,1,a,b))

Q = int(input())
for i in range(Q):
    v, w = map(int,input().split())
    X.append((w,2,v,i))

X.sort(reverse=True)

dsu = DSU(N+1)
ans = [0]*Q

for y,q,a,b in X:
    if q == 1:
        dsu.merge(a,b)
        continue
    ans[b] = dsu.size(a)

for i in ans:
    print(i)