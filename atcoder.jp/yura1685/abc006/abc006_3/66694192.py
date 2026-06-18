N, M = map(int,input().split())

# 大人：2本　老人：3本　赤ちゃん：4本
# すなわち、A+B+C=N, 2*A + 3*B + 4*C = M を満たすA,B,Cを全探索

for B in range(M//3+1):
    left = M - 3*B
    man  = N - B
    if left % 2 == 1:
        continue
    left //= 2
    # A + 2C = left, A+C = man
    C = left - man
    A = 2*man - left
    if A >= 0 and B >= 0 and C >= 0:
        print(A,B,C)
        exit()
print(-1,-1,-1)