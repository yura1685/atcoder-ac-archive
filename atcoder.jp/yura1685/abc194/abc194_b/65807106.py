N = int(input())
A, B = [], []
for _ in range(N):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)

m = 10**6
for i in range(N):
    for j in range(N):
        if i == j:
            m = min(m,A[i]+B[j])
        else:
            m = min(m,max(A[i],B[j]))
print(m)