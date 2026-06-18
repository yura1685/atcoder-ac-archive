from functools import cmp_to_key

N = int(input())
inf = 10**18
P = []
for _ in range(N):
    x, y = map(int,input().split())
    lu, ld = y-1, x
    ru, rd = (y, x-1) if x-1 else (inf, 1)
    P.append((ru,rd, lu,ld))

def compare(a, b):
    v1 = a[0] * b[1]
    v2 = b[0] * a[1]
    if v1 < v2: return -1
    if v1 > v2: return 1
    return 0

P.sort(key=cmp_to_key(compare))

ans = 0
tu, td = 0, 1

for ru, rd, lu, ld in P:
    if tu * ld > td * lu:
        continue
    ans += 1
    tu, td = ru, rd

print(ans)