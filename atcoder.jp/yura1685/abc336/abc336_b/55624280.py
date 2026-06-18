N = int(input())
ans = 0
while N % 2 == 0:
    N = N // 2
    ans += 1
print(ans)