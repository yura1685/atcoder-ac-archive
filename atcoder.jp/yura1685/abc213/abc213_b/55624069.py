N = int(input())
A = list(map(int,input().split()))
rank1 = A.index(max(A))
A.remove(max(A))
rank2 = A.index(max(A))
if rank2 < rank1:
    print(rank2+1)
else:
    print(rank2+2)