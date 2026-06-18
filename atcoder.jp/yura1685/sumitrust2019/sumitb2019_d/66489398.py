from bisect import bisect, bisect_left
N = int(input())
S = input()

num = [[] for _ in range(10)]
for i in range(N):
    num[int(S[i])].append(i)

ans = 0
for start in range(10):
    if not num[start]:
        continue
    for last in range(10):
        if not num[last]:
            continue
        s = num[start][0]
        l = num[last][-1]
        if s > l:
            continue
        for mid in range(10):
            if not num[mid]:
                continue
            if mid in (start,last) and len(num[mid]) == 1:
                continue
            if bisect(num[mid],s) != bisect_left(num[mid],l):
                ans += 1

print(ans)