from more_itertools import run_length

N = int(input())
S = input()

l = list(run_length.encode(S))
d = {}
for i in l:
    s, t = i
    if d.get(s) == None:
        d[s] = t
    else:
        d[s] = max(d[s], t)
    
ans = 0
for i in d:
    ans += d[i]

print(ans)