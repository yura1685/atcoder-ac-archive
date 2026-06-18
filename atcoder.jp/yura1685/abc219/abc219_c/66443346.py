X = input()
alp = 'abcdefghijklmnopqrstuvwxyz'

d = {}
d_r = {}
for i in range(26):
    d[X[i]] = alp[i]
    d_r[alp[i]] = X[i]
ans = []
N = int(input())
for _ in range(N):
    S = input()
    hoge = ''
    for s in S:
        hoge += d[s]
    ans.append(hoge)

ans.sort()

for Y in ans:
    waaa = ''
    for y in Y:
        waaa += d_r[y]
    print(waaa)