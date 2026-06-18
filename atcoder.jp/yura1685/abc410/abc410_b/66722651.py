N, Q = map(int,input().split())
X = list(map(int,input().split()))

box = [0]*N
ans = []
for x in X:
    if x > 0:
        box[x-1] += 1
        ans.append(x)
    else:
        m = box.index(min(box))
        ans.append(m+1)
        box[m] += 1
print(*ans)