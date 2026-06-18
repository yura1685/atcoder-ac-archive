N = int(input())
A = list(map(int,input().split()))
Nuts = 0
for i in range(N):
    if A[i] > 10:
        Nuts += A[i] - 10
print(Nuts)