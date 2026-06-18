from random import randint 
from collections import defaultdict
from statistics import mode

N = int(input())
A = [int(input()) for _ in range(N)]

ans = []
for _ in range(5):
    mod = randint(9*10**9, 10**10)
    d = defaultdict(int)
    for a in A:
        d[a % mod] += 1
    cnt = 0
    for i in d.keys():
        for j in d.keys():
            if d.get(i*j % mod):
                cnt += d[i] * d[j] * d[i*j % mod]
    ans.append(cnt)

print(mode(ans))