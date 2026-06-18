# 6, 8 で10個のとき、大をxとすると、8x+6(10-x)=60+2x
# 同様に、11個のとき、66+2y
# 13個のとき、78+2z
# これらをまとめると、60+2x = 66+2y = 78+2z
# x = 3+y = 9+z

# N X Y
# A1 A2 A3
# Y*a1 + X*(A1-a1) = (Y-X)*a1 + X*A1
# (Y-X)*a1 + X*A1 = (Y-X)*a2 + X*A2 = (Y-X)*a3 + X*A3
# (Y-X)*a1 = (Y-X)*a2 + X*(A2-A1) = (Y-X)*a3 + X*(A3-A1)
# a1 = a2 + X*(A2-A1)/(Y-X) = a3 + X*(A3-A1)/(Y-X)

N, X, Y = map(int,input().split())
A = sorted(map(int,input().split()))
B = [(a-A[0])*X for a in A]
C = []
Z = Y - X
for b in B:
    if b % Z != 0:
        exit(print(-1))
    C.append(b//Z)

M = A[0]
ans = 0

for c in C:
    if c > M:
        exit(print(-1))
    else:
        ans += M - c

print(ans)