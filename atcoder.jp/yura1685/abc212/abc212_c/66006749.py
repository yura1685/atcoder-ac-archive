import bisect

N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort(); B.sort()
B.append(10**20)

ans = 10**9

for a in A:
    l, r = bisect.bisect_left(B, a), bisect.bisect(B, a)
    if l != r:
        print(0)
        exit()
    else:
        ans = min(ans, abs(a-B[l-1]), abs(a-B[l]))

print(ans)