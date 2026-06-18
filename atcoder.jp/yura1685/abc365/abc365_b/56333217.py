N = int(input())
A = list(map(int,input().split()))
A[A.index(max(A))] = 0
print(A.index(max(A))+1)