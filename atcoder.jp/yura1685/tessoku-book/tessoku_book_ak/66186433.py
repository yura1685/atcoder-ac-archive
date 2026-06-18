N, M, B = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

print(M*sum(A)+B*N*M+N*sum(C))