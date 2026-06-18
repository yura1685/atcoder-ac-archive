from itertools import accumulate
from bisect import bisect_left

N, Q = map(int,input().split())
A = [0] + list(map(int,input().split()))
B = [A[i+1]-A[i]-1 for i in range(N)]
C = list(accumulate(B))

for _ in range(Q):
    K = int(input())
    n = bisect_left(C,K)
    if n == 0:
        print(K)
    else:
        hoge = K - C[n-1]
        print(A[n] + hoge)