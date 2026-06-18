from itertools import accumulate
from bisect import *

N = int(input())
A = [2*int(x) for x in input().split()]
S = list(accumulate(A))

ans = 10**18
for i in range(2,N-1):
    X, Y = S[i-1]//2, (S[i-1]+S[-1])//2
    l = bisect(S,X)
    if l == 0:
        l += 1
    elif abs(S[l-1] - X) > abs(S[l] - X):
        l += 1
    r = bisect(S,Y)
    if r == i:
        r += 1
    elif abs(S[r-1] - Y) > abs(S[r] - Y):
        r += 1
    P = S[l-1]
    Q = S[i-1] - S[l-1]
    R = S[r-1] - S[i-1]
    T = S[-1]  - S[r-1]
    ans = min(ans, max(P,Q,R,T) - min(P,Q,R,T))

print(ans//2)