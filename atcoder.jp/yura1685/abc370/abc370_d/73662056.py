from sortedcontainers import SortedList

H, W, Q = map(int,input().split())
X = [SortedList(i for i in range(W)) for _ in range(H)]
Y = [SortedList(i for i in range(H)) for _ in range(W)]

for _ in range(Q):
    h, w = map(int,input().split())
    h, w = h-1, w-1
    if w in X[h]:
        X[h].discard(w)
        Y[w].discard(h)
    else:
        idx_w = X[h].bisect(w)
        
        if idx_w < len(X[h]):
            target_w = X[h][idx_w]
            X[h].pop(idx_w)
            Y[target_w].discard(h)

        if idx_w > 0:
            target_w = X[h][idx_w-1]
            X[h].pop(idx_w-1)
            Y[target_w].discard(h)

        idx_h = Y[w].bisect(h)

        if idx_h < len(Y[w]):
            target_h = Y[w][idx_h]
            Y[w].pop(idx_h)
            X[target_h].discard(w)

        if idx_h > 0:
            target_h = Y[w][idx_h-1]
            Y[w].pop(idx_h-1)
            X[target_h].discard(w)

print(sum(len(x) for x in X))