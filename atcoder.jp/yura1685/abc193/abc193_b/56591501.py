n = int(input())
A = []
P = []
X = []

for i in range(n):
    a, p, x = map(int,input().split())
    A.append(a)
    P.append(p)
    X.append(x)

for i in range(n):
    X[i] -= A[i]
    X[i] = max(X[i],0)

c = []
for i in range(n):
    if X[i] != 0:
        c.append(P[i])

if len(c) == 0:
    print(-1)
else:
    print(min(c))