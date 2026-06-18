from bisect import *

N, L, R = map(int, input().split())
S = input()
cnt = [[] for _ in range(26)]
for i in range(N):
    cnt[ord(S[i]) - 97].append(i)

def solve(Lst):
    res = 0
    for x in Lst:
        yl, yr = x + L, R + x
        res += bisect_right(Lst, yr) - bisect_left(Lst, yl)
    return res

ans = 0
for Lst in cnt:
    if len(Lst) > 1:
        ans += solve(Lst)

print(ans)