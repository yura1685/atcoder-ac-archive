N = int(input())
n = 0
ans = 0
for i in range(N):
    a, b = map(int,input().split())
    ans += a
    n = max(n, b-a)
print(ans+n)