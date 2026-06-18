from collections import defaultdict

d = {}
N, M = map(int,input().split())
coke = []

for _ in range(M):
    A, B = map(int,input().split())
    if d.get(A-B) == None:
        d[A-B] = (A,B)
    else:
        d[A-B] = min(d[A-B],(A,B))

X = []
for key in d.keys():
    X.append((key,d[key][0],d[key][1]))
X.sort()

ans = 0
for _, A, B in X:
    if A > N:
        continue
    c = (N-B)//(A-B)
    ans += c
    N -= (A-B)*c
    if N == 0:
        break

print(ans)