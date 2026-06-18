N = int(input())
ans = 2*(N // 11)
N %= 11
if 0 < N <= 6:
    ans += 1
elif N > 6:
    ans += 2

print(ans)