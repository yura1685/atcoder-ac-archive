from statistics import median_low
N = int(input())
A, B = [], []
for _ in range(N):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)

a_mid = median_low(A)
b_mid = median_low(B)

dis = 0
for i in range(N):
    dis += abs(A[i]-a_mid) + B[i]-A[i] + abs(B[i]-b_mid)
print(dis)