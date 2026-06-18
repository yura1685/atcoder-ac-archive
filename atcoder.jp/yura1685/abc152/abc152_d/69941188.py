from collections import defaultdict

N = int(input())
d = defaultdict(int)

for n in range(1,N+1):
    sn = str(n)
    a, b = sn[0], sn[-1]
    d[(int(a),int(b))] += 1

ans = 0
for a in range(10):
    for b in range(10):
        ans += d[(a,b)] * d[(b,a)]

print(ans)