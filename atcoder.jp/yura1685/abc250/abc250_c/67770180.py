N, Q = map(int,input().split())

A = [i+1 for i in range(N)] # 現在の配列
B = [i-1 for i in range(N+1)] # 数字iはAの何番目か

for _ in range(Q):
    x = int(input())
    if B[x] < N-1:
        y = A[B[x]+1]
        A[B[x]], A[B[y]] = A[B[y]], A[B[x]] 
        B[x], B[y] = B[y], B[x]
    else:
        y = A[B[x]-1]
        A[B[x]], A[B[y]] = A[B[y]], A[B[x]] 
        B[x], B[y] = B[y], B[x]

print(*A)