N, M = map(int, input().split())
Dim = [0] * N
for _ in range(M):
    U, V = map(int, input().split())
    Dim[U-1] += 1
    Dim[V-1] += 1
ans = N * (N-1) // 2
m = 0
for i in range(N):
    m += (N - 1 - Dim[i]) % 2
print(ans - m//2)