N = int(input())
l = len(str(N))
ans = 0
n = 1
while n < l:
    ans += 9*10**(n-1)
    n += 2
if l % 2 == 1:
    ans += N - 10**(n-1) + 1

print(ans)