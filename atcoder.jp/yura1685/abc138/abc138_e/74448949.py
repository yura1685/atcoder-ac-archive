from bisect import bisect_left

S_in = input()
T = input()
S = [[] for _ in range(26)]
for i in range(len(S_in)):
    S[ord(S_in[i]) - 97].append(i+1)
loop = 0
now = 0
for strt in T:
    t = ord(strt) - 97
    if not S[t]: exit(print(-1))
    if S[t][-1] <= now:
        loop += 1
        now = S[t][0]
    else:
        now = S[t][bisect_left(S[t], now + 1)]

print(loop * len(S_in) + now)