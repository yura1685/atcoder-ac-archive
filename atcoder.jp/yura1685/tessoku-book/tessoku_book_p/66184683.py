N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

time = [0]*N
time[1] = A[0]

for i in range(2,N):
    time[i] = min(time[i-1]+A[i-1], time[i-2]+B[i-2])

print(time[-1])