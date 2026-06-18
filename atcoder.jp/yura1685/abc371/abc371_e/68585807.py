N = int(input())
A = list(map(int,input().split()))
app = [[] for _ in range(N+1)]

for i, a in enumerate(A):
    app[a].append(i+1)

ans = 0
for lst in app:
    if not lst:
        continue
    cnt = N*(N+1)//2
    lst = [0] + lst + [N+1]
    for i in range(len(lst)-1):
        cnt -= (lst[i+1] - lst[i]) * (lst[i+1] - lst[i] - 1) // 2
    ans += cnt

print(ans)