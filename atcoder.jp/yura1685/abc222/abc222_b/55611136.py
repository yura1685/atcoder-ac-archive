N, P = map(int,input().split())
L = list(map(int,input().split()))
ans = 0
for i in range(N):
    if L[i] < P:
        ans += 1
print(ans)