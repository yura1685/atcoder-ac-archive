from math import isqrt

N = int(input())

prime = [False,False] + [True]*(N-1)

for p in range(N+1):
    if not prime[p]:
        continue    
    for i in range(2*p,N+1,p):
        prime[i] = False
    
cnt = [0]*(N+1)

for n in range(1,N+1):
    for p in range(2,isqrt(n)+1):
        if not prime[p]:
            continue
        while n % (p*p) == 0:
            n //= p*p
        if n == 1:
            cnt[n] += 1
            break
    else:
        cnt[n] += 1

ans = 0
for c in cnt:
    ans += c*c

print(ans)