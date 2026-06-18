t = "wbwbwwbwbwbw"
w, b = map(int, input().split())
for i in range(len(t)):
    nw = 0
    nb = 0
    for j in range(w + b):
        if t[(i + j) % len(t)] == 'w':
            nw += 1
        else:
            nb += 1
    if w == nw and b == nb:
        print("Yes")
        exit(0)
print("No")
