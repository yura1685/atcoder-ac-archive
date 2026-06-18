from bisect import bisect, bisect_left

d = int(input())
n = int(input())
m = int(input())
store = [0] + [int(input()) for _ in range(n-1)] + [d]
house = [int(input()) for _ in range(m)]
store.sort()

dis = 0
for h in house:
    p = bisect(store,h)
    dis += min(h-store[p-1],store[p]-h)

print(dis)