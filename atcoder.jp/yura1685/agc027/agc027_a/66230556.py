import bisect

N, x = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
s = 0
hoge = []
for a in A:
    s += a
    hoge.append(s)

if x in hoge:
    print(bisect.bisect(hoge, x))
elif hoge[-1] < x:
    print(N-1)
else:
    print(bisect.bisect(hoge,x))