from itertools import *
from bisect import *

N, T = map(int,input().split())
A = [int(x) for x in input().split()]

B, C = A[:N//2], A[N//2:]
Bt, Ct = [], [0]

for P in product((0,1),repeat=len(B)):
    time = 0
    for i in range(len(B)):
        time += B[i]*P[i]
    if time <= T:
        Bt.append(time)

for P in product((0,1),repeat=len(C)):
    time = 0
    for i in range(len(C)):
        time += C[i]*P[i]
    if time <= T:
        Ct.append(time)

Bt.sort()
Ct.sort()

ans = 0
for b in Bt:
    c = Ct[bisect(Ct,T-b)-1]
    ans = max(ans,b+c)

print(ans)