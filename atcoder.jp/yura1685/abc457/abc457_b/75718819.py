N = int(input())
A = []
for _ in range(N):
    L, *B = map(int, input().split())
    A.append(B)
X, Y = map(int, input().split())
print(A[X-1][Y-1])