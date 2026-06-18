from bisect import bisect_left

N = int(input())
A = list(map(int,input().split()))
A.sort()

M = (N-1)*sum(A)
over = 0

for a in A:
    x = N - bisect_left(A,10**8-a)
    over += x
    if a >= 5*10**7:
        over -= 1
over //= 2

print(M - over*10**8)