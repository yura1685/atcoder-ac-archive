from itertools import accumulate

N, Q = map(int,input().split())
X = list(map(int,input().split()))

counter = [0]*(N+1)
cnt = [0]
for x in X:
    if counter[x] == 0:
        cnt.append(cnt[-1]+1)
        counter[x] = 1
    else:
        cnt.append(cnt[-1]-1)
        counter[x] = 0

A = [0]*(N+1)
c = list(accumulate(cnt))

counter = [0]*(N+1)
for i in range(Q):
    x = X[i]
    if counter[x] == 0:
        counter[x] += 1
        A[x] -= c[i]
    else:
        counter[x] -= 1
        A[x] += c[i]

for i in range(1,N+1):
    if counter[i] == 1:
        A[i] += c[-1]
print(*A[1:])