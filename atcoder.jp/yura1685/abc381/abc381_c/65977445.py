#ABC381(C)

from more_itertools import run_length

N = int(input())
S = input()
L = list(run_length.encode(S))
ans = 1

for i in range(1,len(L)-1):
    if L[i-1][0] == '1' and L[i] == ('/',1) and L[i+1][0] == '2':
        x = min(L[i-1][1], L[i+1][1])
        ans = max(ans,2*x+1)

print(ans)


