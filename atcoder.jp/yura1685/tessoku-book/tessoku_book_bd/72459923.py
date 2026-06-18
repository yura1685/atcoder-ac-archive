N, Q = map(int,input().split())
S = input()

L = [0] * (N + 1)
pow_n = [1] * (N+1)

n = 2718281828
mod = 1685*10**17+9

hash = 0
for i in range(N):
    L[i+1] = (L[i] * n + ord(S[i])) % mod
    pow_n[i+1] = (pow_n[i] * n) % mod

for _ in range(Q):
    a, b, c, d = map(int,input().split())
    X = (L[b] - L[a-1]*pow_n[b-a+1]) % mod
    Y = (L[d] - L[c-1]*pow_n[d-c+1]) % mod
    print('Yes' if X == Y else 'No')
