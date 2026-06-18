from collections import defaultdict
N, M = map(int,input().split())
A = list(map(int,input().split()))

up = [defaultdict(int) for _ in range(11)]
do = [defaultdict(int) for _ in range(11)]

for a in A:
    l = len(str(a))
    a %= M
    do[l][a] += 1
    for i in range(11):
        b = a * pow(10,i,M) % M
        up[i][b] += 1

ans = 0
for i in range(11):
    for m in up[i]:
        ans += up[i][m] * do[i][(M-m)%M]

print(ans)