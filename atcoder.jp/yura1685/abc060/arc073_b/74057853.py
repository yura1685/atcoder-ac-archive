from collections import defaultdict

N, W = map(int, input().split())
d = defaultdict(list)
w1 = 0
for _ in range(N):
    w, v = map(int, input().split())
    if not w1: w1 = w
    d[w].append(v)

w2, w3, w4 = w1+1, w1+2, w1+3

for w in [w1, w2, w3, w4]:
    d[w].sort(reverse=True)

n1, n2, n3, n4 = len(d[w1]), len(d[w2]), len(d[w3]), len(d[w4])

ans = 0
for i1 in range(n1+1):
    for i2 in range(n2+1):
        for i3 in range(n3+1):
            for i4 in range(n4+1):
                if w1*i1 + w2*i2 + w3*i3 + w4*i4 > W:
                    continue
                s = 0
                for w, i in [(w1, i1), (w2, i2), (w3, i3), (w4, i4)]:
                    s += sum(d[w][:i])
                ans = max(ans, s)

print(ans)