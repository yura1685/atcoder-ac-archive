L, R = map(int,input().split())

ans = []
l = L
while True:
    i, j = 0, l
    while j % 2 == 0 and j:
        i += 1
        j //= 2
    if l == 0:
        i, j = 60, 0
    r = 2 ** i * (j + 1)
    while r > R:
        i -= 1
        j *= 2
        r = 2 ** i * (j + 1)
    ans.append((l, r))
    if r == R:
        break
    else:
        l = r 

print(len(ans))
for l, r in ans: print(l, r)