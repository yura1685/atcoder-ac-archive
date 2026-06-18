X = [int(input()) for _ in range(6)]
M = min(X[1:])
print((X[0] + M - 1) // M + 4)