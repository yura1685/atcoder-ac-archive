M, K = map(int, input().split())

if M == 0:
    if K == 0:
        print(0, 0)
    else:
        print(-1)
elif M == 1:
    if K == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
else:
    if K >= pow(2, M):
        print(-1)
    else:
        A = [i for i in range(1 << M) if i != K]
        B = [i for i in reversed(range(1 << M)) if i != K]
        print(*(A + [K] + B + [K]))
        