N = int(input())
T = list(map(int,input().split()))
dp = [[False]*(sum(T)+1) for _ in range(N+1)]
dp[0][0] = True
ind = set([0])

for i in range(N):
    t = T[i]
    ind2 = set()
    for x in ind:
        dp[i+1][x] = True
        dp[i+1][x+t] = True
        ind2.add(x+t)
    ind |= ind2

for i in range((sum(T)+1)//2,sum(T)+1):
    if dp[-1][i]:
        exit(print(i))