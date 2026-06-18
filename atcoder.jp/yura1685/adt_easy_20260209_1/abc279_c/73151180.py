H, W = map(int,input().split())
S = sorted(zip(*[input() for _ in range(H)]))
T = sorted(zip(*[input() for _ in range(H)]))
print('Yes' if S == T else 'No')