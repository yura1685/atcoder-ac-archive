N = int(input())
L, R = 0, 168516851685
for _ in range(N):
    Li, Ri = map(int, input().split())
    L = max(L, Li)
    R = min(R, Ri)
    if L <= R:
        print(0)
    else:
        x = (R + L) // 2
        print(max(L-x, 0, x-R))
