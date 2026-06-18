N = int(input())
g:list[list[int]] = [[] for _ in range(N)]
for _ in range(N-1):
    I = input().split()
    u, v = int(I[0])-1, int(I[1])-1
    g[u].append(v)
    g[v].append(u)

cnt:list[list[int]] = [[] for _ in range(N+1)]

stack:list[tuple[int, int, bool]] = [(0, -1, True)]
while stack:
    u, f, b = stack.pop()
    if b == True:
        stack.append((u, f, False))
        for v in g[u]:
            if v == f:
                continue
            stack.append((v, u, True))
    else:
        cnt[f].append(sum(cnt[u]) + 1)

def solve(A: list[int]) -> int:
    dp1, dp2, dp3 = 0, 0, 0
    for a in A:
        dp3 += dp2 * a 
        dp2 += dp1 * a 
        dp1 += a 
    return dp3

ans = 0
for c in cnt:
    sc = N - 1 - sum(c)
    if sc: c.append(sc)
    if len(c) <= 2: continue
    ans += solve(c)

print(ans)