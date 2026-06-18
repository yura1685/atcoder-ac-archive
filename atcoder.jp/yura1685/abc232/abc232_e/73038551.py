H, W, K = map(int, input().split())
mod = 998244353
x1, y1, x2, y2 = map(int,input().split())

a, b, c, d = 1, 0, 0, 0
for _ in range(K):
    a, b, c, d = ((W-1)*b + (H-1)*c) % mod, (a + (W-2)*b + (H-1)*d) % mod, (a + (H-2)*c + (W-1)*d) % mod, (b + c + (H+W-4)*d) % mod

if   (x1, y1) == (x2, y2): print(a)
elif x1 == x2: print(b)
elif y1 == y2: print(c)
else: print(d)