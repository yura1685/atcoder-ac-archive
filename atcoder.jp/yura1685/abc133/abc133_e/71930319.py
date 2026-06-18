from sys import setrecursionlimit
setrecursionlimit(10**8)

N, K = map(int,input().split())
g = [[] for _ in range(N)]
dim = [0] * N
dim[0] = 1
mod = 10**9 + 7

for _ in range(N-1):
    a, b = map(int,input().split())
    a, b = a-1, b-1
    g[a].append(b)
    g[b].append(a)
    dim[a] += 1
    dim[b] += 1

fact = [1] * (max(N,K)+1)
for i in range(1,max(N,K)+1):
    fact[i] = i * fact[i-1] % mod

def P(n,k):
    if n < k: return 0
    return fact[n] * pow(fact[n-k],mod-2,mod) % mod

ans = K
check = [0] * N
check[0] = 1
def dfs(u):
    global ans
    k = dim[u] - 1
    if u == 0:
        ans = ans * P(K-1,k) % mod
    else:
        ans = ans * P(K-2,k) % mod
    for v in g[u]:
        if check[v]: continue
        check[v] = 1
        dfs(v)
dfs(0)

print(ans%mod)