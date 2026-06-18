from collections import Counter

def yura(x):
    n = len(x)
    x.sort()
    key = ''
    for i in range(n):
        alp, num = x[i]
        alp = ord(alp) - ord('a')
        key += '0'*(2-len(str(alp))) + str(alp) + str(num)
    return key

N = int(input())
d = {}

for _ in range(N):
    s = input()
    c = Counter(s)
    hoge = []
    for p in c:
        hoge.append((p,c[p]))
    key = yura(hoge)
    if d.get(key) == None:
        d[key] = 1
    else:
        d[key] += 1

c = list(d.values())
ans = 0
for t in c:
    ans += t*(t-1)//2

print(ans)