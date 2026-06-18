N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A = [0]*(2*M-N) + A

Balance = 0
for i in range(M):
    Balance += (A[i]+A[2*M-1-i])**2

print(Balance)