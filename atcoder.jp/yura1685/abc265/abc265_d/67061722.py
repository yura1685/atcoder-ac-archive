from itertools import accumulate
from bisect import bisect, bisect_left

N, P, Q, R = map(int,input().split())
A = list(map(int,input().split()))
X = [0]+list(accumulate(A))

def In(n):
    if bisect(X,n) != bisect_left(X,n):
        return True
    return False

for i in range(N):
    a = X[i-1]
    if In(a+P) and In(a+P+Q) and In(a+P+Q+R):
        print('Yes')
        exit()
print('No')