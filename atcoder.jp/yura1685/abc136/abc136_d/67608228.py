from bisect import *

S = input()
loop = [i for i in range(len(S)-1) if S[i:i+2] == 'RL']
ans = [0]*len(S)

for i in range(len(S)):
    s = S[i]
    x = bisect_left(loop,i)
    if s == 'R':
        ind = loop[x]
        if (ind-i) % 2 == 0:
            ans[ind] += 1
        else:
            ans[ind+1] += 1
    else:
        ind = loop[x-1]
        if (i-ind) % 2 == 0:
            ans[ind] += 1
        else:
            ans[ind+1] += 1

print(*ans)