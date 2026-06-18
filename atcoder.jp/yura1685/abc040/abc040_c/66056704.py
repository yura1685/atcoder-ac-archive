N = int(input())
a = list(map(int,input().split()))
dp = [0]*N
dp[1] = abs(a[1]-a[0])

for i in range(2,N):
    x = abs(a[i]-a[i-2])
    y = abs(a[i]-a[i-1])
    dp[i] = min(x+dp[i-2], y+dp[i-1])

print(dp[-1])