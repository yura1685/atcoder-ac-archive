from collections import defaultdict

N, K, M = map(int, input().split())

color = defaultdict(list)
for _ in range(N):
    C, V = map(int, input().split())
    color[C].append(V)

A = []
B = []

for c in color:
    color[c].sort(reverse=True)
    A.append(color[c][0])
    for v in color[c][1:]:
        B.append(v)

A.sort(reverse=True)
B.sort(reverse=True)

ans = sum(A[:M])
C = A[M:] + B
C.sort(reverse=True)
ans += sum(C[:K-M])

print(ans)