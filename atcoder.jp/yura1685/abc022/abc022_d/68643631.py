N = int(input())

agx, agy, bgx, bgy = 0, 0, 0, 0
A, B = [], []

for _ in range(N):
    Ax, Ay = map(int,input().split())
    agx += Ax
    agy += Ay
    A.append((Ax, Ay))

for _ in range(N):
    Bx, By = map(int,input().split())
    bgx += Bx
    bgy += By
    B.append((Bx, By))

AM, BM = 0, 0
for i in range(N):
    x, y = A[i]
    AM = max(AM, (agx-x*N)**2 + (agy-y*N)**2)
    x, y = B[i]
    BM = max(BM, (bgx-x*N)**2 + (bgy-y*N)**2)

print((BM/AM)**(0.5))