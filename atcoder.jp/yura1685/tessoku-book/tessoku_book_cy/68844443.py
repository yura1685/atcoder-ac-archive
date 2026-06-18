N = int(input())
prime = [False, False] + [True] * (N-1)

for p in range(2,N+1):
    if not prime[p]:
        continue
    for i in range(2*p,N+1,p):
        prime[i] = False

for i in range(N+1):
    if prime[i]: print(i)