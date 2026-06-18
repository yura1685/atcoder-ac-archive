from bisect import bisect, bisect_left

N = int(input())
box = [0]

for _ in range(N):
    w = int(input())
    if box[-1] < w:
        box.append(w)
    else:
        c = bisect(box,w)
        d = bisect_left(box,w)
        if c != d:
            pass
        else:
            box[c] = w
            box.sort()

print(len(box)-1)