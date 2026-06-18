b = list(map(int,input().split()))
d = {}
d_rev = {}
for i in range(10):
    d[b[i]] = i
    d_rev[i] = b[i]

N = int(input())

def trans(s :str):
    ans = ''
    for i in s:
        ans += str(d[int(i)])
    return int(ans)

def snart(s :str):
    ans = ''
    for i in s:
        ans += str(d_rev[int(i)])
    return int(ans)

A = [(trans(input()),i) for i in range(N)]
A.sort()
B = [(snart(str(x)),y) for x, y in A]

for i, j in B:
    print(i)