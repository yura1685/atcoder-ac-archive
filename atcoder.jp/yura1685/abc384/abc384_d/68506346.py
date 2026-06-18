from itertools import accumulate

N, S = map(int,input().split())
A = list(map(int,input().split()))
sa = sum(A)
S %= sa
A += A
B = set(accumulate(A))
for b in B:
    if b + S in B:
        exit(print('Yes'))
print('No')