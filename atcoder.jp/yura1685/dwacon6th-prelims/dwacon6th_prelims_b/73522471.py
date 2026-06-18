mod = 10**9 + 7
N = int(input())
X = list(map(int,input().split()))
inv = [0] + [pow(i,mod-2,mod) for i in range(1,N+1)]
f = 1
for i in range(1,N):
    f = f * i % mod

Sinv = [0]
for i in range(1,N+1):
    Sinv.append((Sinv[i-1] + inv[i]) % mod)

ans = 0
for i in range(N-1):
    ans += (X[i+1] - X[i]) * Sinv[i+1] * f % mod

print(ans % mod)