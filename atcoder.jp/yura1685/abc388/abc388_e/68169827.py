from sortedcontainers import SortedList

N = int(input())
A = list(map(int,input().split()))
ans = 0

up = A[:N//2]
lo = SortedList(A[N//2:])
l = (N+1)//2

for a in up:
    b = lo.bisect_left(2*a)
    if b == l:
        break
    lo.pop(b)
    l -= 1
    ans += 1

print(ans)