from more_itertools import run_length
S = input()
E = list(run_length.encode(S))
L = len(E)

ans = 0
for i in range(L-1):
    x, y = int(E[i][0]), int(E[i+1][0])
    if y != x + 1: continue
    n, m = E[i][1], E[i+1][1]
    ans += min(n,m)

print(ans)