import bisect

N = int(input())
X = list(map(int,input().split()))
P = list(map(int,input().split()))
Q = int(input())

c = [0]*(N+1)
for i in range(N):
    c[i+1] = c[i] + P[i]

for _ in range(Q):
    L, R = map(int,input().split())
    l = bisect.bisect_left(X,L)
    r = bisect.bisect_right(X,R)
    print(c[r] - c[l])