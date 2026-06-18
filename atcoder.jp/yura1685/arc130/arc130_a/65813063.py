from more_itertools import run_length

N = int(input())
S = input()

def c(n):
    return n*(n-1)//2

L = list(run_length.encode(S))
ans = 0

for x in L:
    ans += c(x[1])

print(ans)