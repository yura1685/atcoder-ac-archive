from math import isqrt

N = int(input())

L = [2]*(N)
L[0], L[1] = 0, 1

for i in range(2,isqrt(N)+1):
    for j in range(i,N):
        if i*j >= N:
            break
        if i == j:
            L[i*j] += 1
        else:
            L[i*j] += 2

ans = 0
for i in range(1,(N+1)//2):
    ans += 2*L[i]*L[N-i]

if N % 2 == 0:
    ans += L[N//2]*L[N//2]

print(ans)