N, M = map(int,input().split())
L = list(map(int,input().split()))

def win(W):
    line = 1
    width = 0
    for i in range(N):
        l = L[i]
        if width + l > W:
            width = 0
            line += 1
        if width + l == W:
            width = 0
            if i != N-1:
                line += 1
        elif width + l < W:
            width += l + 1
    return line

l, r = max(L)-1, 10**20+1
while (r-l) > 1:
    mid = (r+l)//2
    if win(mid) >= M+1:
        l = mid
    else:
        r = mid

print(r)