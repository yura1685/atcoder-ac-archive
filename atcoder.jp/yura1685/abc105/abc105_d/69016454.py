from collections import defaultdict

N, M = map(int,input().split())
A = list(map(int,input().split()))
B = [0]*(N+1)

for i in range(N):
    B[i+1] = (B[i] + A[i]) % M

D = defaultdict(int)
ans = 0
for i in range(N+1):
    b = B[i]
    ans += D[b]
    D[b] += 1

print(ans)