from more_itertools import run_length

S = input()
if S[0] == '>':
    S = '<' + S
if S[-1] == '<':
    S = S + '>'
    
c = list(run_length.encode(S))
n = len(c)

def f(n):
    return n*(n+1)//2
ans = 0
for i in range(n-1):
    if c[i][0] == '<':
        ans += f(c[i][1]-1) + f(c[i+1][1]-1) + max(c[i][1],c[i+1][1]) 

print(ans)