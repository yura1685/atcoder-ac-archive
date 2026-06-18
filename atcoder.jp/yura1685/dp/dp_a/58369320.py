N = int(input())
h = list(map(int,input().split()))
dp = [0,abs(h[1]-h[0])]
for i in range(N-2):
    a = abs(h[i+2]-h[i]) + dp[i]
    b = abs(h[i+2]-h[i+1]) + dp[i+1]
    dp.append(min(a,b))
print(dp[-1])