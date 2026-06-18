def get_canonical(poly):
    min_x = min(p[0] for p in poly)
    min_y = min(p[1] for p in poly)
    return tuple(sorted((p[0] - min_x, p[1] - min_y) for p in poly))

def generate_fixed_polyominoes(n):
    if n <= 0:
        return set()
    if n == 1:
        return {((0, 0),)}

    prev_polys = generate_fixed_polyominoes(n - 1)
    next_polys = set()

    for poly in prev_polys:
        neighbors = set()
        for x, y in poly:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in poly:
                    neighbors.add((nx, ny))
        
        for neighbor in neighbors:
            new_poly = poly + (neighbor,)
            next_polys.add(get_canonical(new_poly))
            
    return next_polys

N = int(input())
K = int(input())
Polyomino = generate_fixed_polyominoes(K)

S = [input() for _ in range(N)]

ans = 0
for P in Polyomino:
    for dh in range(N):
        for dw in range(N):
            for h, w in P:
                nh, nw = h + dh, w + dw
                if not (0 <= nh < N and 0 <= nw < N) or S[nh][nw] == '#':
                    break
            else:
                ans += 1

print(ans)