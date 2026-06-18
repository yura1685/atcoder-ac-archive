from bisect import *

T = int(input())

P = []
for i in range(0,58):
    for j in range(i+1,59):
        for k in range(j+1,60):
            P.append(2**i + 2**j + 2**k)
P.sort()

def solve(x):
    if x < 7:
        return -1
    return P[bisect(P,x)-1]    

for _ in range(T):
    N = int(input())
    print(solve(N))