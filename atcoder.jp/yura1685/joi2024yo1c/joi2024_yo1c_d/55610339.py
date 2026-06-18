K = int(input())
N = int(input())
A = list(map(int,input(). split()))
M = int(input())
B = list(map(int, input(). split()))
ans = 0
for i in range(N):
    for j in range(M):
        if A[i] + K == B[j]:
            ans += 1
print(ans)