from collections import defaultdict

S = list(input())
mod = 0
d = defaultdict(int)
d[0] += 1
for i in range(len(S)):
    mod = (mod + int(S[-i-1]) * pow(10,i,2019)) % 2019
    d[mod] += 1

ans = 0
for v in d.values():
    ans += v*(v-1)//2

print(ans)