N = int(input())
A = [int(input()) for _ in range(N)]

if A[0]: exit(print(-1))

flag = True
ans = 0
for i in range(N-1):
    if A[i+1] > A[i] + 1:
        flag = False
        break
    if A[i] >= A[i+1]:
        ans += A[i]
if flag:
    ans += A[N-1]

print(ans if flag else -1)