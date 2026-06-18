from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
d = defaultdict(int)
for a in A: d[a] += 1
ans = 0

for x in d:
    if d[x] == 1:
        continue
    p = d[x]*(d[x]-1)//2
    ans += p*(N-d[x])

print(ans)