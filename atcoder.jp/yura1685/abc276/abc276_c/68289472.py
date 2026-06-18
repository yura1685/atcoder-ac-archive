# 考察パート
# 数列を後ろから見ていき、単調増加でない区間を探す（存在する）
# 3 1 2 <- 3 1 の部分で単調非増加。
# 3の次に小さい2を先頭に持ってきて、その他を降順ソートすればよい。
# つまり、3 1 2 -> 2 3 1
# 9 8 6 5 10 3 1 2 4 7
# の場合は、3 1 2 4 7 の部分がそれであり
# 3 1 2 4 7 -> 2 7 4 3 1
# となる

N = int(input())
P = list(map(int,input().split()))
Q = []
for i in range(N-1):
    Q.append(P[-i-1])
    if P[-i-2] < P[-i-1]:
        continue
    Q.append(P[-i-2])
    n = Q[-1]
    for j in range(n-1,0,-1):
        if j in Q:
            Q.remove(j)
            Q.sort(reverse=True)
            Q = [j] + Q
            break
    R = P[:-i-2] + Q
    print(*R)
    break