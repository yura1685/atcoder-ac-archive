N, A, B = map(int,input().split())
X = list(map(int,input().split()))

tir = 0
for i in range(N-1):
    tir += min(A*(X[i+1]-X[i]), B)

print(tir)