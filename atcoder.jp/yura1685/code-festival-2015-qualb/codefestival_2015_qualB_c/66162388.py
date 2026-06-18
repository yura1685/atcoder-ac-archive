N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort(reverse=True); B.sort(reverse=True)

if N < M:
    print('NO')
    exit()

for i in range(M):
    if B[i] > A[i]:
        print('NO')
        exit()
print('YES')