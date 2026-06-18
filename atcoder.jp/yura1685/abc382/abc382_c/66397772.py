from bisect import bisect

N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

eat = [A[0]]
for i in range(1,N):
    eat.append(min(A[i],eat[i-1]))

eat.reverse()

for b in B:
    c = bisect(eat, b)
    if c != 0:
        print(N-c+1)
    else:
        print(-1)