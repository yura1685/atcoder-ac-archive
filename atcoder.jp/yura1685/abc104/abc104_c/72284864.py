from itertools import product
from sortedcontainers import SortedList

D, G = map(int,input().split())
G //= 100
prob = []
for i in range(1,D+1):
    p, c = map(int,input().split())
    prob.append((p,c//100))

ans = 1685
for P in product([0,1],repeat=D):
    score = 0
    cnt = 0
    SL = SortedList()
    for i in range(D):
        if P[i]:
            score += prob[i][0] * (i+1) + prob[i][1]
            cnt += prob[i][0]
        else:
            SL.add((i+1,prob[i][0]))
    if score >= G:
        ans = min(ans, cnt)
        continue
    while score < G and SL:
        s, p = SL.pop()
        if p == 1:
            continue
        score += s
        cnt += 1
        p -= 1
        SL.add((s,p))
    if score >= G:
        ans = min(ans, cnt)

print(ans)