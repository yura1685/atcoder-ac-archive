N = int(input())
A = int(input())
B = int(input())

ans = 0
for i in range(1,N+1):
    if (i % A == 0 and i % B != 0) or (i % A != 0 and i % B == 0):
        ans += 1

print(ans)