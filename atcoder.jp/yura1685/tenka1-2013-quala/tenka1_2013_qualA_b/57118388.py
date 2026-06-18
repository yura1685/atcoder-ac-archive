N = int(input())
rank_A = 0
for i in range(N):
    V, W, X, Y, Z = map(int,input().split())
    S = V + W + X + Y + Z
    if S < 20:
        rank_A += 1
print(rank_A)