N = int(input())
A = list(map(int,input().split()))
B = sorted(A)
ans = 0
for i in range(N):
    ans += i * B[i] - (N-1-i) * A[i]
print(ans)