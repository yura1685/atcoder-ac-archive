from itertools import accumulate

N, M = map(int,input().split())
kabe = [0]*(N+1)
for _ in range(M):
    L, R = map(int,input().split())
    kabe[L-1] += 1
    kabe[R] -= 1

c = list(accumulate(kabe))
print(min(c[:-1]))