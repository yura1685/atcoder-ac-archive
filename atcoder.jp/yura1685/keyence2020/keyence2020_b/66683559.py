N = int(input())

a = []
for _ in range(N):
    X, L = map(int, input().split())
    a.append((X+L,X-L))
a.sort()

last = -10**10
ans = 0

for T, S in a:
    if last <= S:
        ans += 1
        last = T

print(ans)