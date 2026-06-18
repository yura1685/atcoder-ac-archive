N = int(input())
A = list(map(int,input().split()))
s2 = 0
s = 0
for i in range(N):
    s2 += A[i]*A[i]
    s += A[i]

print((s*s-s2)//2)