N = int(input())
A = [0] + list(map(int,input().split()))
ans = [-1] * N + [N]

for i in range(N,0,-1):
    ans[i] = ans[A[i]] if i < A[i] else i

print(*ans[1:])