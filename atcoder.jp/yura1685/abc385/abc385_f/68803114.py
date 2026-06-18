from fractions import Fraction

N = int(input())
B = []
for _ in range(N):
    X, H = map(int,input().split())
    B.append((X,H))

# y = -x1*(h2-h1)/(x2-x1)+h1

ans = -1
for i in range(N-1):
    x1, h1 = B[i]
    x2, h2 = B[i+1]
    H = -Fraction(x1*(h2-h1),x2-x1) + h1
    ans = max(ans,H)

print(float(ans) if ans >= 0 else -1)