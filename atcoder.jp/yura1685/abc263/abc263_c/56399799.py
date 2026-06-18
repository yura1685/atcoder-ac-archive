import itertools

N, M = map(int,input().split())

C = [] 
for i in range(1,M+1):
    C.append(i)

L = list(itertools.combinations(C,N))
for i in L:
    print(*i)