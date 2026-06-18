from itertools import product

N = int(input())
A = list(map(int,input().split()))

if N == 1:
    print(A[0]); exit()

ans = float('inf')
for p in product((0,1),repeat=N-1):
    XOR = 0
    OR = A[0]
    for i in range(N-1):
        if p[i] == 0:
            OR |= A[i+1]
        else:
            XOR ^= OR
            OR = A[i+1]
    XOR ^= OR
    ans = min(ans,XOR)

print(ans)