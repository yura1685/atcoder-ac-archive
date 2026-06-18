from sortedcontainers import SortedList

SL = SortedList()
c = 0
ans = 0
new = []
l, r = -float('inf'), float('inf')
Len = 0

Q = int(input())
for _ in range(Q):
    q,*a = map(int,input().split())
    if q == 1:
        SL.add(a[0])
        Len += 1
        c += a[1]
        if l <= a[0] <= r:
            pass
        else:
            ans += min(abs(a[0]-r),abs(a[0]-l))
        l, r = SL[(Len-1)//2], SL[Len//2]
    else:
        print(l,ans+c)