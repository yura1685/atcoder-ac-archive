Q = int(input())
box = []
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        box.append(int(q[1]))
    else:
        print(min(box))
        box.pop(box.index(min(box)))