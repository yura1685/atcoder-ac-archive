import sympy

N = int(input())
A = list(map(int,input().split()))

p_list = list(sympy.primerange(2,max(A)+1))
GCD, p = 0, 0

for prime in p_list:
    count = 0
    for a in A:
        if a % prime == 0: # type: ignore
            count += 1
    if count >= GCD:
        GCD = count
        p = prime

print(p)