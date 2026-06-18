from collections import defaultdict
import heapq

N = int(input())
slime = []
heapq.heapify(slime)
d = defaultdict(int)

for _ in range(N):
    S, C = map(int,input().split())
    heapq.heappush(slime,S)
    d[S] += C

ans = 0
while slime:
    S = heapq.heappop(slime)
    C = d[S]
    ans += C % 2
    if C != 1:
        if d[2*S] == 0:
            d[2*S] += C//2
            heapq.heappush(slime,2*S)
        else:
            d[2*S] += C//2

print(ans)