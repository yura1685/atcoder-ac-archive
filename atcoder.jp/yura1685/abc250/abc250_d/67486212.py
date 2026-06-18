from itertools import accumulate

def eratosthenes(n):
    is_prime = [False, False] + [True]*(n-1)
    for p in range(2,n+1):
        if not is_prime[p]:
            continue
        for k in range(p*2, n+1, p):
            is_prime[k] = False
    return is_prime

N = int(input())

prime = eratosthenes(int(N**(1/3))+10)
prime_ac = list(accumulate(prime))

ans = 0
for p in range(1,N):
    if p**4 >= N:
        break
    if not prime[p]:
        continue
    qmax = int((N//p)**(1/3))
    if (qmax+1)**3 <= N//p:
        qmax += 1
    ans += prime_ac[qmax] - prime_ac[p]

print(ans)