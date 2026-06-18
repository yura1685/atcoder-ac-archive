from sortedcontainers import SortedList

mod = 10 ** 9 + 7
N, A, B = map(int, input().split())
S = SortedList(map(int, input().split()))
if N == 1:
    ans = S[0] * pow(A, B, mod) % mod
    exit(print(ans))
if A == 1:
    ans = [s % mod for s in S]
    exit(print(*ans, sep='\n'))

while B:
    s = S.pop(0)
    B -= 1
    if s * A < S[-1]:
        S.add(s * A)
    else:
        S.add(s * A)
        break

if B == 0:
    ans = [s % mod for s in S]
    exit(print(*ans, sep='\n'))

S1, S2 = S[:B%N], S[B%N:]
time = B // N
ans1 = [s * pow(A, time, mod) % mod for s in S2]
ans2 = [s * pow(A, time+1, mod) % mod for s in S1]
print(*(ans1 + ans2), sep='\n')