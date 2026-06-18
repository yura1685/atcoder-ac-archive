A, B, C = map(int,input().split())

dp = [[[0]*101 for _ in range(101)] for _ in range(101)]

for x in range(99,-1,-1):
    for y in range(99,-1,-1):
        for z in range(99,-1,-1):
            w = x+y+z
            if w == 0:
                continue
            dp[x][y][z] = (x/w)*dp[x+1][y][z] + (y/w)*dp[x][y+1][z] + (z/w)*dp[x][y][z+1]+1

print(dp[A][B][C])