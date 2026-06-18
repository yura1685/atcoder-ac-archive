N, M, P, Q, R = map(int,input().split())

choco = [[] for _ in range(N)]
for _ in range(R):
    x, y, z = map(int,input().split())
    choco[x-1].append((y-1,z))

def solve(X):
    dansi = [0] * M
    for x in X:
        for y, z in choco[x]:
            dansi[y] += z
    dansi.sort(reverse=True)
    return sum(dansi[:Q])

ans = 0
for i in range(1<<N):
    if i.bit_count() != P:
        continue
    josi = [j for j in range(N) if (i >> j) & 1]
    ans = max(ans, solve(josi))

print(ans)