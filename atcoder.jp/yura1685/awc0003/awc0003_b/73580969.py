N = int(input())
l, r = '', ''
ans = 0
for _ in range(N):
    L, R = input().split()
    if r == L:
        ans += 1
    l, r = L, R
print(ans)