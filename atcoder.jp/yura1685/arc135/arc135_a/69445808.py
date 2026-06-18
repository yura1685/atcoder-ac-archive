from collections import defaultdict

X = int(input())
d = defaultdict(int)
d[X] += 1

while d:
    M = max(d.keys())
    if M <= 4:
        break
    C = d[M]
    d.pop(M)
    d[M//2] += C
    d[(M+1)//2] += C

ans = 1
mod = 998244353

for key in d.keys():
    ans *= pow(key,d[key],mod)

print(ans % mod)