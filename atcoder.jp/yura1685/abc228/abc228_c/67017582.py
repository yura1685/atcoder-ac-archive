N, K = map(int,input().split())
score = []
for _ in range(N):
    P = list(map(int,input().split()))
    score.append(sum(P))

A = score.copy()
A.sort(reverse=True)
c = A[K-1]
for s in score:
    if s+300 >= c:
        print('Yes')
    else:
        print('No')