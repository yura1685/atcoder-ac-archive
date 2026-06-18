N = int(input())
ans = 1685

for _ in range(N):
    t = int(input())
    ans = min(ans, t)

print(ans)