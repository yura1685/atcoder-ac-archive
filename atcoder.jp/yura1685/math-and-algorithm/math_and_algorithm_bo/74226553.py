from collections import defaultdict

N, X, Y = map(int, input().split())
d = defaultdict(set)
for n in range(1, N+1):
    for m in range(n, N+1):
        d[n+m].add(n*m)

for a_b in range(2, 2*N+1):
    c_d = X - a_b
    for ab in d[a_b]:
        for cd in d[c_d]:
            if ab * cd == Y:
                exit(print('Yes'))
print('No')