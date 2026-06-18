from more_itertools import run_length
from math import comb

N = int(input())
S = input()

c = list(run_length.encode(S))
ans = 0
for x in c:
    ans += comb(x[1],2)

print(comb(N,2)-ans)