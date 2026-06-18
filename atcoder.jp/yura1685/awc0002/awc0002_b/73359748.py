N, M, K = map(int,input().split())
A = list(map(int,input().split()))
B =  set(map(int,input().split()))
ans = [A[i-1] for i in range(1,N+1) if i in B and A[i-1] < K]
print(len(ans), sum(ans))