N = int(input())
A = list(map(int,input().split()))
A.sort()

import bisect

ans = 0
hoge = 0
for a in A:
    if a == 50000:
        hoge += 1
        continue
    c = 100000 - a
    ans += bisect.bisect(A,c) - bisect.bisect_left(A,c)

print(ans//2 + hoge*(hoge-1)//2)