N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
left = []
need = 0
ans = 0
for i in range(N):
    a, b = A[i], B[i]
    if a > b:
        left.append(a - b)
    if a < b:
        need += b - a
        ans += 1

if sum(left) < need:
    print(-1)
else:
    left.sort()
    while need > 0:
        x = left.pop()
        ans += 1
        need -= x
    print(ans)