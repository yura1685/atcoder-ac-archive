N, W = map(int,input().split())
A = list(map(int,input().split()))
c = []
for i in range(N):
    if A[i] <= W:
        c.append(A[i])

for i in range(N-1):
    for j in range(i+1,N):
        if A[i]+A[j] <= W:
            c.append(A[i]+A[j])

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if A[i]+A[j]+A[k] <= W:
                c.append(A[i]+A[j]+A[k])

print(len(set(c)))