N = int(input())

prime = [2]
for n in range(2,N+1):
    for p in prime:
        if p**2 > n:
            prime.append(n)
            break
        if n % p == 0:
            break

print(*prime[1:])