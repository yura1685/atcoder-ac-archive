N = int(input())
D = [[0]*N for _ in range(N)]
for i in range(N-1):
    l = list(map(int,input().split()))
    for j in range(i+1,N):
        D[i][j] = D[j][i] = l[j-i-1]

dp = [0 for _ in range(1<<N)]
for mask in range(1 << N):
    n = mask.bit_count()
    if n & 1 == 1:
        continue
    bit = [i for i in range(N) if (mask >> i) & 1]
    for i in range(n-1):
        for j in range(i+1,n):
            x = (1 << bit[i]) + (1 << bit[j])
            dp[mask] = max(dp[mask], dp[mask^x] + D[bit[i]][bit[j]])

print(max(dp))