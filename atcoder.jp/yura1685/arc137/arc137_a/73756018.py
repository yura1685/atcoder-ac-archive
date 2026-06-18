from math import gcd

L, R = map(int,input().split())
D = R - L
for d in range(D,0,-1):
    for l in range(L,R-d+1):
        r = l + d 
        if gcd(l, r) == 1:
            exit(print(d))