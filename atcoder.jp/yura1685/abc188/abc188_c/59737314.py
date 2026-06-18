N = int(input())
A = list(map(int,input().split()))
print(A.index(min(max(A[2**(N-1):]),max(A[:2**(N-1)])))+1)