N, K = map(int, input().split())
Theme = []
for _ in range(N):
    M = int(input())
    s = set(input().split())
    Theme.append(s)

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if len(Theme[i] & Theme[j]) >= K:
            ans += 1

print(ans)