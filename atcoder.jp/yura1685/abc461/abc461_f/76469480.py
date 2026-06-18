N = int(input())
mod = 998244353

if N == 1:
    exit(print(1))

D = []
i = 2
while i * i <= N:
    if N % i == 0:
        D.append(i)
        if i * i != N:
            D.append(N // i)
    i += 1
D.append(N)
D.sort()

fact = [1] * 20
for i in range(1, 20):
    fact[i] = (fact[i - 1] * i) % mod

ans = 0
def dfs(left, sum, cnt, idx):
    global ans
    
    for i in range(idx, len(D)):
        d = D[i]
        if d * d >= left:
            if left >= d:
                n_sum = (sum + left) % mod
                n_lcnt = cnt + 1
                ans += (fact[n_lcnt] * n_sum) % mod
                ans += (fact[n_lcnt + 1] * (n_sum + 1)) % mod
                ans %= mod
            break
            
        if left % d == 0:
            dfs(left // d, sum + d, cnt + 1, i + 1)

dfs(N, 0, 0, 0)
print(ans)