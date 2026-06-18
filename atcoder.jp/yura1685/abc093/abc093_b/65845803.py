A, B, K = map(int,input().split())
x = []
for i in range(A,A+K):
    if i <= B:
        x.append(i)
for j in range(B-K+1,B+1):
    if A <= j:
        x.append(j)
c = list(set(x))
c.sort()
for i in c:
    print(i)