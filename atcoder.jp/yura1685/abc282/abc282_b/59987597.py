def can(x,y):
    m = len(x)
    for i in range(m):
        if x[i] == y[i] == 'x':
            return 0
    return 1


N, M = map(int,input().split())
solve = []
ans = 0

for _ in range(N):
    solve.append(input())

for x in range(N-1):
    for y in range(x+1,N):
        ans += can(solve[x],solve[y])

print(ans)