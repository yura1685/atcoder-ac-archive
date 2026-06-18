N = int(input())
A = list(map(int,input().split()))

m, k = 1000, 0
for i in range(N-1):
    if A[i] >= A[i+1]:
        continue
    k = m // A[i]
    m %= A[i]
    m += k*A[i+1]
    k = 0

print(m)