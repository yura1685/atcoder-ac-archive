from bisect import *

N, T = input().split()
N = int(N)

S = [input() for _ in range(N)]

def bubun(s,t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
    return j

mae = [bubun(s,T) for s in S]
T = T[::-1]
usiro = [bubun(s[::-1],T) for s in S]

usiro.sort()

n = len(T)
ans = 0

def f(i):
    return N - bisect_left(usiro,n-i)

for i in mae:
    ans += f(i)

print(ans)