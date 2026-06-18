from itertools import accumulate

N = int(input())
A = [0] + list(map(int,input().split()))
B = [0] + list(map(int,input().split()))
C = [0] + list(map(int,input().split()))
SA = list(accumulate(A))
SB = list(accumulate(B))
SC = list(accumulate(C))

X = [SA[i] - SB[i] for i in range(N+1)]
Y = [SB[i] - SC[i] for i in range(N+1)]

ans = -float('inf')

maxx = -float('inf')
for y in range(2, N):
    hoge = X[y-1]
    maxx = max(maxx, hoge)
    ans = max(ans, maxx + Y[y])

print(ans + SC[-1])