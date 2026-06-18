def solve() -> int:
    I = input().split()
    X, Y, Z = int(I[0]), int(I[1]), int(I[2])
    H = int(input())
    mx, Mx, my, My, mz, Mz = X, 0, Y, 0, Z, 0
    for _ in range(H):
        I = input().split()
        x, y, z = int(I[0]), int(I[1]), int(I[2])
        mx = min(mx, x)
        Mx = max(Mx, x)
        my = min(my, y)
        My = max(My, y)
        mz = min(mz, z)
        Mz = max(Mz, z)
    a, b, c, d, e, f = mx, my, mz, X-Mx-1, Y-My-1, Z-Mz-1
    return a ^ b ^ c ^ d ^ e ^ f

N = int(input())

xor = 0
for _ in range(N):
    xor ^= solve()
print('WIN' if xor else 'LOSE')