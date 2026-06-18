N, K =map(int,input().split())
T = []
for _ in range(N):
    T.append(list(map(int,input().split())))

import itertools
arr = [i+2 for i in range(N-1)]

X = list(itertools.permutations(arr))

ans = 0
for i in range(len(X)):
    time = 0
    c = [1] + list(X[i]) + [1]
    for j in range(len(c)-1):
        time += T[c[j]-1][c[j+1]-1]
    if time == K:
        ans += 1
print(ans)