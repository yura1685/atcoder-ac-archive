from bisect import bisect

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort(); B.sort(); C.sort()

saidan = 0
for b in B:
    saidan += bisect(A,b-1)*(N-bisect(C,b))
print(saidan)