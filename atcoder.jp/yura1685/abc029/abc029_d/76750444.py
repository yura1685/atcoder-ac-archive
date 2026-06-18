N = int(input()) + 1
ans = 0
for i in range(10):
    shuki = 10 ** (i + 1)
    x, y = divmod(N, shuki)
    ans += x * 10 ** i
    y -= 10 ** i
    if y > 0:
        ans += min(y, 10 ** i)
print(ans)