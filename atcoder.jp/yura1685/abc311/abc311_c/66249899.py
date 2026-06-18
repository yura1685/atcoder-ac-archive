import sys
sys.setrecursionlimit(10**9)

N = int(input())
A = list(map(int, input().split()))

d = {}
for i in range(N):
    d[i+1] = A[i]

c = [0]*(N+1)

def dfs(u):
    if c[d[u]] == 0:
        c[d[u]] = 1
        return dfs(d[u])
    else:
        return d[u]
    
x = dfs(1)
ans = [x]
y = d[x]
while y != x:
    ans.append(y)
    y = d[y]
print(len(ans))
print(*ans)