N = int(input())
z, w = [], []
M, m = max, min
for _ in range(N):
    x, y = map(int,input().split())
    z.append(x+y)
    w.append(x-y)

print(M(M(z)-m(z),M(w)-m(w)))