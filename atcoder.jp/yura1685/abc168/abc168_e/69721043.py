from math import gcd

d = dict()
N = int(input())
cnt = 0

for _ in range(N):
    A, B = map(int,input().split())
    if 0 in (A,B):
        if (A,B) == (0,0):
            cnt += 1
        elif d.get(0):
            if A == 0:
                d[0][0] += 1
            else:
                d[0][1] += 1
        else:
            if A == 0:
                d[0] = [1,0]
            else:
                d[0] = [0,1]   
        continue 
    g = gcd(A,B)
    A, B = A//g, B//g
    if A < 0:
        A, B = -A, -B
    if B > 0:
        a, b = A, B
    else:
        a, b = -B, A
    if d.get((a,b)):
        if B > 0:
            d[(a,b)][0] += 1
        else:
            d[(a,b)][1] += 1
    else:
        if B > 0:
            d[(a,b)] = [1,0]
        else:
            d[(a,b)] = [0,1]

mod = 10 ** 9 + 7

ans = 1
for a, b in d.values():
    ans = ans * (pow(2,a,mod) + pow(2,b,mod) - 1) % mod

print((ans-1+cnt)%mod)