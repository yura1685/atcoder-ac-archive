N, T = map(int,input().split())
A = []
for _ in range(N):
    c = int(input())
    A.append(c)

time = 0
for i in range(N-1):
    if A[i+1] >= A[i] + T:
        time += T
    else:
        time += A[i+1] - A[i]
time += T
print(time)