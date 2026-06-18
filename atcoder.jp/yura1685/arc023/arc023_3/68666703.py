from sys import setrecursionlimit
from functools import cache
from more_itertools import run_length
setrecursionlimit(10**8)

N = int(input())
A = list(map(int,input().split()))
mod = 10**9 + 7
    
def comb(n,k):
    bunsi = 1
    bunbo = 1
    for i in range(1,k+1):
        bunsi *= n - i + 1
        bunbo *= i
        bunsi, bunbo = bunsi % mod, bunbo % mod
    return bunsi * pow(bunbo,mod-2,mod) % mod

B = list(run_length.encode(A))

ans = 1
for i in range(len(B)):
    if B[i][0] == -1:
        ans *= comb(B[i+1][0] - B[i-1][0] + B[i][1], B[i][1])
        ans %= mod

print(ans)