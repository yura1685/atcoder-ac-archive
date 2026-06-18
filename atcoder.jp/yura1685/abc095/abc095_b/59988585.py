N, X = map(int,input().split())
ans = 0
c = []
for i in range(N):
    m = int(input())
    ans += 1
    X -= m
    c.append(m)
m = min(c)
print(ans + X//m)