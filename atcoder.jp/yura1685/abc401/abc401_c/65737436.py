def Kib(n,k):
    if n < k:
        return 1
    f = [k]
    for _ in range(k):
        f.append((2*f[-1]-1) % (10**9))
    for i in range(n-2*k):
        f.append((2*f[-1] - f[i]) % (10**9))
    return f[n-k]

N, K = map(int,input().split())
print(Kib(N,K))