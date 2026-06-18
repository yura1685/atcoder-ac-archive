N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort(); B.sort()

dis = 0
for i in range(N):
    dis += abs(A[i]-B[i])

print(dis)