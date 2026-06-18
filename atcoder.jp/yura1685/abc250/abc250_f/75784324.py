N = int(input())

P = []
for _ in range(N):
    X, Y = map(int, input().split())
    P.append((4*X, 4*Y))

def area(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    return abs((x2-x1) * (y3-y1) - (x3-x1) * (y2-y1)) // 2

S = 0
for i in range(1, N-1):
    S += area(P[0], P[i], P[i+1])
S //= 4
ans = 4*S

X = area(P[0], P[1], P[2])
l, r = 0, 2
while True:
    ans = min(ans, abs(S-X))
    if (r - l) % N == 2 or X < S:
        X += area(P[l%N], P[r%N], P[(r+1)%N])
        r += 1
    else:
        X -= area(P[l%N], P[(l+1)%N], P[r%N])
        l += 1
    ans = min(ans, abs(S-X))
    if l > 2 * N:
        break

print(ans // 2)