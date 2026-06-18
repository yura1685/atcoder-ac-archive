from bisect import bisect_right as b_r

S, T = input(), input()
N = len(S)
idx = [[] for _ in range(26)]
for i, s in enumerate(S):
    idx[ord(s) - 97].append(i)
for i in range(26):
    idx[i].append(N)

ans = 0
for i in range(N):
    j = i - 1
    for t in T:
        j = idx[ord(t) - 97][b_r(idx[ord(t) - 97], j)]
        if j == N: break
    ans += j - i

print(ans)