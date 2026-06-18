from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))
d = defaultdict(int)

for a in A:
    if a-1 in d:
        d[a] = max(d[a], d[a-1]+1)
    else:
        d[a] = max(d[a], 1)

print(max(d.values()))