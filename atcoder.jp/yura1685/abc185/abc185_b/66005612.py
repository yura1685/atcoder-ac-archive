N, M, T = map(int,input().split())

bat = N
time = [tuple(map(int,input().split())) for _ in range(M)]

for c in range(M):
    if c == 0:
        a, b = time[c]
        bat -= a
        if bat <= 0:
            print('No')
            exit()
        bat += b - a
        bat = min(bat, N)
        last = b
    else:
        a, b = time[c]
        bat -= (a - last)
        if bat <= 0:
            print('No')
            exit()
        else:
            bat += (b-a)
            bat = min(bat, N)
            last = b

bat -= (T - last)
print('Yes' if bat > 0 else 'No')