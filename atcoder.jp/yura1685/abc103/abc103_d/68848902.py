N, M = map(int,input().split())
X = []
for _ in range(M):
    a, b = map(int,input().split())
    X.append((b,a))
X.sort()

ans = 0
l = 0
for b, a in X:
    if a <= l < b:
        continue
    ans += 1
    l = b-1

print(ans)