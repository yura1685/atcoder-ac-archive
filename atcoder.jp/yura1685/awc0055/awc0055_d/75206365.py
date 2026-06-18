from sortedcontainers import SortedList

sl = SortedList()
Q = int(input())
ans = 0
for _ in range(Q):
    q, x = input().split()
    x = int(x)
    if q == '+':
        sl.add(x)
    else:
        if sl[(len(sl)-1)//2] == x:
            ans += 1
        sl.remove(x)
print(ans)