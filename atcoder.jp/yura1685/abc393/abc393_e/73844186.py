class Sieve_of_Eratosthenes:
    def __init__(self, n: int) -> None:
        self.n = [False, False] + [True] * (n - 1)
        self.primes:list[int] = []
        for i in range(2,n+1):
            if not self.n[i]: continue
            self.primes.append(i)
            for j in range(2*i,n+1,i):
                self.n[j] = False

N, K = map(int, input().split())
A = list(map(int, input().split()))
M = max(A)
P = Sieve_of_Eratosthenes(M).primes

cnt = [0] * (M+1)
for a in A:
    cnt[a] += 1
for p in P:
    for i in range(M//p, 0, -1):
        cnt[i] += cnt[i*p]

ans = [0] * (M+1)
for i in range(1, M+1):
    if cnt[i] >= K:
        ans[i] = i
for p in P:
    for i in range(1, M//p + 1):
        if ans[i*p] < ans[i]:
            ans[i*p] = ans[i]

for a in A:
    print(ans[a])