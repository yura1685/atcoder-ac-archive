N = int(input())

cnt = 0
ans = 0
for i in range(N):
    A = int(input())
    if A != 0:
        cnt += A
    else:
        ans += cnt//2
        cnt = 0
ans += cnt//2

print(ans)