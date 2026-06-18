N, K = map(int, input().split())
R, S, P = map(int, input().split())
d = {'r':P, 's':R, 'p':S}
T = input()
Hands = [T[i::K]+'x' for i in range(K)]

ans = 0
for H in Hands:
    last = 'x'
    for i in range(len(H)-1):
        h = H[i]
        if h != last:
            ans += d[h]
            last = h
        else:
            last = 'x'

print(ans)