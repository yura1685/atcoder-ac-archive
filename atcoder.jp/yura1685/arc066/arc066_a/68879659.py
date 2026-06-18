from collections import Counter

N = int(input())
A = list(map(int, input().split()))
mod = 10**9 + 7
C = Counter(A)

if N % 2 == 1:
    if not (all([C[i] == 2 for i in range(2,N,2)]) and C[0] == 1):
        print(0)
    else:
        print(pow(2,N//2,mod))

else:
    if not all([C[i] == 2 for i in range(1,N,2)]):
        print(0)
    else:
        print(pow(2,N//2,mod))