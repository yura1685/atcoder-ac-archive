import bisect

N = int(input())
A = list(map(int,input().split()))
A.sort()

ans = 0
for i in range(N+1):
    if bisect.bisect_left(A,i) <= N-i:
        ans = i
print(ans)