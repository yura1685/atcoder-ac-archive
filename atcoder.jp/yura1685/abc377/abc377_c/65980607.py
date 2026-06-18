def f(x,y,n):
    if 1 <= x <= n and 1 <= y <= n:
        return (x,y)
    return None

N, M = map(int,input().split())

cant = set()

for _ in range(M):
    a, b = map(int,input().split())
    for dx, dy in [(-2, +1), (-2, -1), (-1, +2), (-1, -2),
                   (0, 0),
                   (+1, +2), (+1, -2), (+2, +1), (+2, -1)]:
        s = f(a+dx, b+dy, N)
        if s is not None:
            cant.add(s)

print(N*N - len(set(cant)))