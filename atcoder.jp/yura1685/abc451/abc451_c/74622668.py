from heapq import heappush, heappop

Q = int(input())
tree = []
ans = 0
for _ in range(Q):
    q, h = map(int, input().split())
    if q == 1:
        heappush(tree, h)
        ans += 1
    else:
        while tree and tree[0] <= h:
            heappop(tree)
            ans -= 1
    print(ans)