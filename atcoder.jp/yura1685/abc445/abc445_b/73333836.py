N = int(input())
S = [input() for _ in range(N)]
L = max(len(s) for s in S)

for s in S:
    dot = (L - len(s)) // 2
    print('.'*dot + s + '.'*dot)