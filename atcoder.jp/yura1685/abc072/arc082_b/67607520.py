N = int(input())

p = [int(x) for x in input().split()]
b = [p[i] != i+1 for i in range(N)]

ans = 0
for i in range(N-1):
    if not b[i]:
        b[i], b[i+1] = True, True
        ans += 1
if not b[-1]:
    ans += 1

print(ans)