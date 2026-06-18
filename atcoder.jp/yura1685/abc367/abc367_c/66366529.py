from itertools import product

N, K = map(int,input().split())
R = list(map(int,input().split()))
r = [[j for j in range(1,i+1)] for i in R]

for c in product(*r):
    if sum(c) % K == 0:
        print(*c)