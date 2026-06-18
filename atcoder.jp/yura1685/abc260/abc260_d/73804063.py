from sortedcontainers import SortedList

N, K = map(int,input().split())
P = [int(x)-1 for x in input().split()]
upper = SortedList()
lower = [-1] * N
ans = [-1] * N
hei = [0] * N

for turn in range(1,N+1):
    pick = P[turn-1]
    idx = upper.bisect(pick)
    if idx == len(upper):
        upper.add(pick)
        hei[pick] = 1
    else:
        num = upper[idx]
        upper.discard(num)
        upper.add(pick)
        hei[pick] = hei[num] + 1
        lower[pick] = num
    if hei[pick] == K:
        upper.discard(pick)
        u = pick
        while u != -1:
            ans[u] = turn
            u = lower[u]

print(*ans, sep='\n')