N = int(input())
A = list(map(int,input().split()))
humidai = 0
for i in range(1,N):
    if A[i-1] > A[i]:
        humidai += A[i-1] - A[i]
        A[i] = A[i-1]
print(humidai)